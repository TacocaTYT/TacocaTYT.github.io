const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./posts.db');

let sql = 'SELECT ID, TITLE, BLURB, BODY, IMAGE FROM POSTS ORDER BY ID DESC LIMIT 1';

db.get(sql, (err, row) => {
  if (err) {
    return console.error(err.message);
  }
  return row
    ? console.log(row.ID, row.TITLE, row.BLURB, row.BODY, row.IMAGE)
    : console.log('No posts found in the database');
});

// close the database connection
db.close();