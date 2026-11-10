create table categories (
    -- id serial primary key,
    id integer generated always as identity primary key,
    name text not null
);

create table priorities (
    id integer generated always as identity primary key,
    code text not null unique,
    name text not null
);

create table statuses (
    id integer generated always as identity primary key,
    code text not null unique,
    name text not null
);

create table tasks (
    id integer generated always as identity primary key,
    title text not null,
    description text,
    category_id integer not null references categories(id),
    priority_id integer not null references priorities(id),
    status_id integer not null references statuses(id)
)
