db.createUser({
  user: "sheltr",
  pwd: "sheltr",
  roles: [{ role: "readWrite", db: "sheltr" }],
});
