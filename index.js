const sqlite3 = require('sqlite3').verbose();

const rpb = document.getElementById("recentPostButton");

const postTitle = "404";
let db = new sqlite3.Database('./posts.db');

let sql = 'SELECT ID, TITLE FROM POSTS ORDER BY ID DESC LIMIT 1';

db.get(sql, (err, row) => {
    if (err) {
      return console.error(err.message);
    }
    if (row) {
      const postTitle = row.TITLE;
      const postURL = "404";
      rpb.textContent = postTitle;
      rpb.href = postURL;
    } else {
      console.log('No posts found in the database');
    }
  });