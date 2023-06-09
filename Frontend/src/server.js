// server.js
const express = require('express');
const cors = require('cors');

const app = express();

// Enable CORS
app.use(cors());

// Rest of your server-side code

// Start the server
app.listen(8000, () => {
  console.log('Server is running on port 8000');
});
