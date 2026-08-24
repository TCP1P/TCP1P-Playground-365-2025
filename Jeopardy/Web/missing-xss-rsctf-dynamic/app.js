const http = require('node:http')

http
  .createServer((request, response) => {
    const url = new URL(request.url, 'http://127.0.0.1')
    const params = Object.create(null)
    url.searchParams.forEach((value, key) => {
      params[key] = value.replaceAll('\\', '\\\\').replaceAll('</', '<\\/').replaceAll('"', '\\"')
    })
    const value = `
<html>
<body></body>
<script>
  const name = "${params.name}"
  document.body.innerText = name
</script>
</html>`
    response.writeHead(200, { 'content-type': 'text/html' })
    response.end(value)
  })
  .listen(3000, '127.0.0.1')
