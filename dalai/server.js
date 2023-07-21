const Dalai = require('dalai')

console.log('Starting server...')
new Dalai().serve(process.env.DALAI_PORT)
console.log('Server stopped')