import socketio
import time as time
import config


class Dalai:

    sio = socketio.Client()

    def __init__(self):
        self.RESULTS = {}
        self.REQ_IDS = []
        self.CURRENT_ID = None
        self.MOST_RECENT_WORD = None
        self.DONE = False
        self.RESULT = None
        self.setup()

    def setup(self):
        while True:
            try:
                print('Connecting to ' + config.DALAI_URI)
                self.sio.connect(config.DALAI_URI)
                break
            except Exception as e:
                print(f"Connection failed: {e}. Retrying in 1 second...")
                time.sleep(1)

        print('Connected')
        self.call_backs()

    def call_backs(self):
        @self.sio.on('result')
        def on_request(data):
            # Get this request ID
            req_id = data.get('request', {}).get('id')
            new_word = data.get('response', '')
            self.CURRENT_ID = req_id

            # And if it's not already in results
            if req_id not in self.RESULTS:
                # then initially stuff it with this data
                self.RESULTS[req_id] = data
                # and add this request id to the last
                self.REQ_IDS.append(req_id)
            # If it's already in results
            else:
                # then simply add the new response word
                self.RESULTS[req_id]['response'] += new_word

            self.MOST_RECENT_WORD = str(new_word).strip()
            if self.MOST_RECENT_WORD == "<end>" or self.MOST_RECENT_WORD == "\n":
                self.DONE = True
                if self.REQ_IDS and self.RESULTS:
                    # get latest id
                    req_id = self.REQ_IDS[-1]
                    # get result dictionary from latest id as key
                    result = self.RESULTS[req_id]
                    # return result
                    self.RESULT = result

    def generate(self, request):
        self.sio.emit('request', request)
        while not self.DONE:
            time.sleep(0.01)

        # Reset Vars
        self.RESULTS = {}
        self.REQ_IDS = []
        self.CURRENT_ID = None
        self.MOST_RECENT_WORD = None
        self.DONE = False

        return self.RESULT

    def generate_request(self, prompt, model, id='0', n_predict=128, repeat_last_n=64, repeat_penalty=1.3, seed=-1, temp=0.5, threads=4, top_k=40, top_p=0.9):
        request = {'debug': False, 'id': id, 'model': model, 'models': [model], 'n_predict': n_predict, 'prompt': prompt, 'repeat_last_n': repeat_last_n, 'repeat_penalty': repeat_penalty, 'seed': seed, 'temp': temp, 'threads': threads, 'top_k': top_k, 'top_p': top_p}
        return request

    def request(self, prompt, prettify=True):
        if prettify is False:
            return self.generate(prompt)

        else:
            response = self.generate(prompt)['response']
            response = response.replace("\n", "")
            response = response.replace("\r", "")
            response = response.replace("<end>", "")
            if not response.endswith("."):
                response += "."
            return response
