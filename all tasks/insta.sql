create schema instagram;
set search_path to instagram;

create table users
(
    user_id serial primary key,
    username varchar(50) not null unique,
    email varchar(100) not null unique,
    password_hash varchar(255) not null,
    created_at timestamp default current_timestamp
);

create table posts
(
    post_id serial primary key,
    user_id int not null,
    content text,
    created_at timestamp default current_timestamp,
    foreign key (user_id) references users(user_id) on delete cascade
);

create table comments
(
    comment_id serial primary key,
    post_id int not null,
    user_id int not null,
    content text not null,
    created_at timestamp default current_timestamp,
    foreign key (post_id) references posts(post_id) on delete cascade,
    foreign key (user_id) references users(user_id) on delete cascade
);

create table likes
(
    like_id serial primary key,
    post_id int not null,
    user_id int not null,
    liked_at timestamp default current_timestamp,
    unique (post_id, user_id),
    foreign key (post_id) references posts(post_id) on delete cascade,
    foreign key (user_id) references users(user_id) on delete cascade
);

create table saved_posts
(
    saved_post_id serial primary key,
    user_id int not null,
    post_id int not null,
    saved_at timestamp default current_timestamp,
    unique (user_id, post_id),
    foreign key (user_id) references users(user_id) on delete cascade,
    foreign key (post_id) references posts(post_id) on delete cascade
);

create table followers
(
    follower_id int not null,
    followed_id int not null,
    unique (followed_id, follower_id),
    constraint no_equal_follower_ids
        check (follower_id != followed_id),
    foreign key (follower_id) references users(user_id) on delete cascade,
    foreign key (followed_id) references users(user_id) on delete cascade
);
