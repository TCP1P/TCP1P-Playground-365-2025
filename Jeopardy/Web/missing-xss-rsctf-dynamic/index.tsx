import "react"
Bun.serve({
    host: "0.0.0.0",
    port: 3000,
    fetch(req) {
        const url = new URL(req.url)
        let params = Object.create(null)
        url.searchParams.forEach((value, key)=>{
            params[key] = value.replaceAll("\\", "\\\\").replaceAll("</", "<\\/").replaceAll('"', '\\"')
        })
        let value = `
<html>
<body></body>
<script>
  const name = "${params['name']}"
  document.body.innerText = name
</script>
</html>`
        const res = new Response(value)
        res.headers.set("content-type", 'text/html')
        return res
    },
})
