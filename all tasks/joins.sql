SELECT u.username, COUNT(p.id) AS post_count
FROM "user" u
         LEFT JOIN post p ON u.id = p.user_id
GROUP BY u.id, u.username
HAVING COUNT(p.id) >= 2;

SELECT u.username, COUNT(f.followed_id) AS followed_count
FROM "user" u
         LEFT JOIN followers f ON u.id = f.follower_id
GROUP BY u.id, u.username;

SELECT p.title, COUNT(l.user_id) AS like_count
FROM post p
         LEFT JOIN "like" l ON p.id = l.post_id
GROUP BY p.id, p.title;

SELECT p.title, COUNT(c.id) AS comment_count
FROM post p
         LEFT JOIN comment c ON p.id = c.post_id
GROUP BY p.id, p.title;

SELECT p.title, COUNT(sp.user_id) AS saved_count
FROM post p
         LEFT JOIN saved_post sp ON p.id = sp.post_id
GROUP BY p.id, p.title;

SELECT u.username, COUNT(l.post_id) AS like_count
FROM "user" u
         LEFT JOIN "like" l ON u.id = l.user_id
GROUP BY u.id, u.username;

SELECT u.username, COUNT(sp.post_id) AS saved_post_count
FROM "user" u
         LEFT JOIN saved_post sp ON u.id = sp.user_id
GROUP BY u.id, u.username;

SELECT u.username, COUNT(c.id) AS comment_count
FROM "user" u
         LEFT JOIN comment c ON u.id = c.user_id
GROUP BY u.id, u.username;

SELECT u.username, COUNT(f.follower_id) AS follower_count
FROM "user" u
         LEFT JOIN followers f ON u.id = f.followed_id
GROUP BY u.id, u.username;
