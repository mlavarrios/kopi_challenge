create table if not exists messages (
    id uuid primary key default gen_random_uuid(),
    conversation_id text not null,
    role text not null,
    message text not null,
    created_at timestamp default now()
);

create table if not exists test (
    id uuid primary key default gen_random_uuid(),
    conversation_id text not null,
    role text not null,
    message text not null,
    created_at timestamp default now()
);
