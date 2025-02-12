import express from 'express'
import { readdirSync, statSync,  writeFileSync, readFileSync } from 'fs'
import { join } from 'path'

const app = express()
const PORT = 3000

app.get('/', (req, res) => {
  const script = `<script>
    fetch('/api/files')
      .then(res => res.json())
      .then(files => {
        const list = document.createElement('ul')
        files.forEach(file => {
          const item = document.createElement('li')
          item.textContent = file
          item.addEventListener('click', () => {
            fetch('/api/files/' + file)
              .then(res => res.text())
              .then(text => {
                document.getElementById('content').textContent = text
              })
          })
          list.appendChild(item)
        })
        document.body.appendChild(list)
      })
    </script>`

    const body = `<div id="content"></div>`
    const createForm = `<form action="/api/files" method="POST">
    <input type="text" name="filename" />
    <textarea name="content"></textarea>
    <button type="submit">Create</button>
    </form>`
    const style = `<style>
    body {
      font-family: Arial, sans-serif;
    }
    form {
      margin-top: 1rem;
    }
    textarea {
      width: 100%;
      height: 10rem;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    </style>`
    res.send(style + body + createForm + script)
})

app.get('/api/files', (req, res) => {
  const files = readdirSync(join(__dirname, 'files'))
    .filter((file) => statSync(join(__dirname, 'files', file)).isFile())
    .map((file) => file.replace('.txt', ''))
  res.json(files)
})

app.get('/api/files/:filename', (req, res) => {
    let { filename } = req.params
    const content = readFileSync(join(__dirname, 'files', filename + ".txt"),)
    res.send(content)
})

app.post('/api/files', express.urlencoded({ extended: true }), (req, res) => {
  const { filename, content } = req.body
  writeFileSync(join(__dirname, 'files', filename + ".txt"), content)
  res.redirect('/')
})

app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`)
})