const express = require('express');
const app = express();
const port = 80;
const host = '65.108.212.2';


app.get('/', (req, res) => {
res.send('Hello, World');
});

app.listen(port, () => {
console.log(`Server is running on http://${host}:${port}`);
});