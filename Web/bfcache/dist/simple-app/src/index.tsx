import { Hono } from 'hono'
import { readFileSync } from 'fs'
import { sessionMiddleware, Session } from 'hono-sessions'
import { BunSqliteStore } from 'hono-sessions/bun-sqlite-store'
import { Database } from 'bun:sqlite'

const app = new Hono()
const db = new Database('./database.sqlite')
const store = new BunSqliteStore(db)

app.use('*', sessionMiddleware({
  store
}))

app.use(async (c, next) => {
  c.setRenderer((content) => {
    return c.html(
      <html>
        <head>
          <title>Simple Note App</title>
          <meta http-equiv="Content-Security-Policy" content={`default-src 'self'`} />
        </head>
        <body>
          {content}
        </body>
      </html>
    )
  })
  await next()
})

app.post('/api/note', async (c) => {
  const session = await c.get('session' as never) as Session
  const { note } = await c.req.json()
  session.set('note', note)
  return c.json({ success: true })
})


app.use("/api/*", async (c, next) => {
  const referer = c.req.header("referer")
  const url = new URL(c.req.url)
  if (!referer?.startsWith(url.origin)) {
    return c.render(
      <div>
        <h1>403 - Permission Denied</h1>
      </div>
    )
  }
  await next()
})

app.get('/api/note', async (c) => {
  const session = await c.get('session' as never) as Session
  const note = (session.get('note') || '') as string
  return c.html(note)
})


app.get('/', async (c) => {
  return c.render(
    <div>
      <h1>Simple Note App</h1>
      <form id="note-form">
        <textarea id="note-content"></textarea>
        <button type="button">Save Note</button>
      </form>
      <div id="note-display"></div>
      <script src='/script.js'></script>
    </div>
  )
})

app.get('/script.js', async (c) => c.text(await readFileSync("./src/script.js").toString()))

app.get('*', async (c) => {
  c.status(404)
  return c.render(
    <div>
      <h1>404 - Page Not Found</h1>
    </div>
  )
})

export default app
