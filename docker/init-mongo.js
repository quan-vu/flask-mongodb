db.createUser(
    {
        user: "myadmin",
        pwd : "mypassword",
        roles: [
            {
                role: "readWrite",
                db  : "mytestdb"
            }
        ]
    }
)