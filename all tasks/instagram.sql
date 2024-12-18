SELECT COUNT(*) AS posts_count
FROM posts
WHERE user_id = 'user_id_here';

SELECT COUNT(*) AS followed_count
FROM follows
WHERE follower_id = 'user_id_here';

SELECT COUNT(*) AS likes_count
FROM likes
WHERE post_id = 'post_id_here';

SELECT COUNT(*) AS comments_count
FROM comments
WHERE post_id = 'post_id_here';

SELECT COUNT(*) AS saved_count
FROM saves
WHERE post_id = 'post_id_here';

SELECT COUNT(*) AS user_likes_count
FROM likes
WHERE user_id = 'user_id_here';

SELECT COUNT(*) AS user_saved_posts_count
FROM saves
WHERE user_id = 'user_id_here';

SELECT COUNT(*) AS user_comments_count
FROM comments
WHERE user_id = 'user_id_here';

SELECT COUNT(*) AS followers_count
FROM follows
WHERE followed_id = 'user_id_here';
