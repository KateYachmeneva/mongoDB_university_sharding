sh.addShard("shard1ReplSet/shard1:27018");
sh.addShard("shard2ReplSet/shard2:27019");

sh.enableSharding("university");

db = db.getSiblingDB("university");

db.students.createIndex({ student_id: "hashed" });

sh.shardCollection("university.students", { student_id: "hashed" });

print("Sharding configured successfully");
sh.status();