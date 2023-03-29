import sqlite3 from 'sqlite3';
const rpb = document.getElementById("recentPostButton");
const db = new sqlite3.Database('./posts.db', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the database.');
});

const sql = 'SELECT ID, TITLE FROM POSTS ORDER BY ID DESC LIMIT 1';

db.get(sql, (err, row) => {
  if (err) {
    return console.error(err.message);
  }
  if (row) {
    const postTitle = row.TITLE;
    const postURL = `/posts/${row.ID}`;
    rpb.textContent = postTitle;
    rpb.href = postURL;
  } else {
    console.log('No posts found in the database');
    rpb.postTitle = "404"
    rpb.href = "404"
  }
  db.close();
});