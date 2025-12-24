create table HeatMaster_applications
(
    id          integer      not null
        primary key autoincrement,
    status      varchar(120) not null,
    description varchar(120) not null,
    part        varchar(120) not null,
    phone       varchar(120) not null
);

create table HeatMaster_blog
(
    id       integer      not null
        primary key autoincrement,
    article  varchar(200) not null,
    text     text         not null,
    date     datetime     not null,
    final    text         not null,
    start    text         not null,
    text_two text         not null
);

create table HeatMaster_calculateprice
(
    id          integer      not null
        primary key autoincrement,
    subject     varchar(120) not null,
    procedure   varchar(120) not null,
    stage       varchar(120) not null,
    type        varchar(120) not null,
    produce     varchar(120) not null,
    type_across varchar(120) not null,
    install     varchar(120) not null,
    name        varchar(120) not null,
    phone       varchar(120) not null,
    history     varchar(120) not null
);

create table HeatMaster_commentblog
(
    id       integer      not null
        primary key autoincrement,
    text     varchar(500) not null,
    date     datetime     not null,
    author   varchar(320) not null,
    username varchar(320) not null,
    rating   real         not null,
    blog_id  bigint       not null
        references HeatMaster_blog
            deferrable initially deferred
);

create index HeatMaster_commentblog_blog_id_1c451b34
    on HeatMaster_commentblog (blog_id);

create table HeatMaster_heatedmats
(
    id       integer      not null
        primary key autoincrement,
    name     varchar(120) not null,
    count    integer      not null,
    price    integer      not null,
    fullname varchar(120) not null,
    status   varchar(120) not null
);

create table HeatMaster_history
(
    id          integer      not null
        primary key autoincrement,
    operator    varchar(120) not null,
    status      varchar(120) not null,
    description varchar(120) not null,
    data        date         not null
);

create table HeatMaster_historyapplication
(
    id             integer      not null
        primary key autoincrement,
    status         varchar(120) not null,
    description    varchar(120) not null,
    operator       varchar(120) not null,
    application_id bigint       not null
        references HeatMaster_applications
            deferrable initially deferred
);

create index HeatMaster_historyapplication_application_id_0e9b34f7
    on HeatMaster_historyapplication (application_id);

create table HeatMaster_hotcable
(
    id     integer      not null
        primary key autoincrement,
    name   varchar(120) not null,
    count  integer      not null,
    price  real         not null,
    image  varchar(100),
    status varchar(120) not null
);

create table HeatMaster_imageblog
(
    id      integer      not null
        primary key autoincrement,
    image   varchar(100),
    status  varchar(120) not null,
    blog_id bigint       not null
        references HeatMaster_blog
            deferrable initially deferred
);

create index HeatMaster_imageblog_blog_id_594a5b34
    on HeatMaster_imageblog (blog_id);

create table HeatMaster_letscooperate
(
    id          integer      not null
        primary key autoincrement,
    name        varchar(120) not null,
    phone       varchar(120) not null,
    email       varchar(254) not null,
    status      varchar(120) not null,
    operator    varchar(120) not null,
    description varchar(120) not null
);

create table HeatMaster_methodpay
(
    id          integer       not null
        primary key autoincrement,
    icon        varchar(100),
    description varchar(1000) not null
);

create table HeatMaster_part
(
    id      integer      not null
        primary key autoincrement,
    image   varchar(100),
    title   varchar(120) not null,
    text    text         not null,
    blog_id bigint       not null
        references HeatMaster_blog
            deferrable initially deferred
);

create index HeatMaster_part_blog_id_8308b37c
    on HeatMaster_part (blog_id);

create table HeatMaster_produce
(
    id          integer       not null
        primary key autoincrement,
    icon        varchar(100),
    name        varchar(120)  not null,
    description varchar(1000) not null,
    sphere      varchar(120)  not null,
    date_work   varchar(10)   not null
);

create table HeatMaster_thermostats
(
    id   integer      not null
        primary key autoincrement,
    type varchar(120) not null,
    icon varchar(100)
);

create table HeatMaster_thermostat
(
    id                   integer        not null
        primary key autoincrement,
    image                varchar(100),
    name                 varchar(120)   not null,
    price                real           not null,
    manufacturer         varchar(120)   not null,
    country_manufacturer varchar(120)   not null,
    model                varchar(120)   not null,
    description          varchar(12000) not null,
    description_block    varchar(12000) not null,
    charge_block         varchar(120)   not null,
    control_range        varchar(120)   not null,
    max_load             varchar(120)   not null,
    type_connection      varchar(120)   not null,
    type_device          varchar(120)   not null,
    thermostats_id       bigint         not null
        references HeatMaster_thermostats
            deferrable initially deferred,
    available            integer        not null
);

create index HeatMaster_thermostat_thermostats_id_4054bc0d
    on HeatMaster_thermostat (thermostats_id);

create table HeatMaster_thermostatimages
(
    id                  integer not null
        primary key autoincrement,
    image               varchar(100),
    thermostat_image_id bigint  not null
        references HeatMaster_thermostat
            deferrable initially deferred
);

create index HeatMaster_thermostatimages_thermostat_image_id_f3dce4e8
    on HeatMaster_thermostatimages (thermostat_image_id);

create table HeatMaster_warmfloor
(
    id          integer       not null
        primary key autoincrement,
    logo        varchar(100),
    name        varchar(120)  not null,
    image       varchar(100),
    description varchar(1000) not null,
    model       varchar(120)  not null,
    history     varchar(1000) not null
);

create table HeatMaster_modelrange
(
    id             integer      not null
        primary key autoincrement,
    name           varchar(120) not null,
    length         integer      not null,
    power          varchar(120) not null,
    price          real         not null,
    model_range_id bigint       not null
        references HeatMaster_warmfloor
            deferrable initially deferred
);

create index HeatMaster_modelrange_model_range_id_53128100
    on HeatMaster_modelrange (model_range_id);

create table auth_group
(
    id   integer      not null
        primary key autoincrement,
    name varchar(150) not null
        unique
);

create table auth_user
(
    id           integer      not null
        primary key autoincrement,
    password     varchar(128) not null,
    last_login   datetime,
    is_superuser bool         not null,
    username     varchar(150) not null
        unique,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     bool         not null,
    is_active    bool         not null,
    date_joined  datetime     not null,
    first_name   varchar(150) not null
);

create table HeatMaster_cart
(
    id         integer  not null
        primary key autoincrement,
    created_at datetime not null,
    updated_at datetime not null,
    user_id    integer  not null
        references auth_user
            deferrable initially deferred
);

create index HeatMaster_cart_user_id_5d6ebdf2
    on HeatMaster_cart (user_id);

create table HeatMaster_cartitem
(
    id            integer          not null
        primary key autoincrement,
    quantity      integer unsigned not null,
    cart_id       bigint           not null
        references HeatMaster_cart
            deferrable initially deferred,
    thermostat_id bigint           not null
        references HeatMaster_thermostat
            deferrable initially deferred,
    check ("quantity" >= 0)
);

create index HeatMaster_cartitem_cart_id_d4ab61a4
    on HeatMaster_cartitem (cart_id);

create unique index HeatMaster_cartitem_cart_id_thermostat_id_c4a10bb6_uniq
    on HeatMaster_cartitem (cart_id, thermostat_id);

create index HeatMaster_cartitem_thermostat_id_a489459d
    on HeatMaster_cartitem (thermostat_id);

create table HeatMaster_order
(
    id               integer      not null
        primary key autoincrement,
    created_at       datetime     not null,
    updated_at       datetime     not null,
    status           varchar(20)  not null,
    total_amount     real         not null,
    shipping_address varchar(500) not null,
    comment          varchar(500) not null,
    user_id          integer      not null
        references auth_user
            deferrable initially deferred
);

create index HeatMaster_order_user_id_a3cb2bb1
    on HeatMaster_order (user_id);

create table HeatMaster_orderitem
(
    id                integer          not null
        primary key autoincrement,
    quantity          integer unsigned not null,
    price_at_purchase real             not null,
    order_id          bigint           not null
        references HeatMaster_order
            deferrable initially deferred,
    thermostat_id     bigint           not null
        references HeatMaster_thermostat
            deferrable initially deferred,
    check ("quantity" >= 0)
);

create index HeatMaster_orderitem_order_id_6ec6295b
    on HeatMaster_orderitem (order_id);

create index HeatMaster_orderitem_thermostat_id_9f917a0d
    on HeatMaster_orderitem (thermostat_id);

create table HeatMaster_thermostatcomment
(
    id            integer          not null
        primary key autoincrement,
    text          varchar(1000)    not null,
    rating        integer unsigned not null,
    created_at    datetime         not null,
    updated_at    datetime         not null,
    thermostat_id bigint           not null
        references HeatMaster_thermostat
            deferrable initially deferred,
    user_id       integer          not null
        references auth_user
            deferrable initially deferred,
    check ("rating" >= 0)
);

create index HeatMaster_thermostatcomment_thermostat_id_4e2814bf
    on HeatMaster_thermostatcomment (thermostat_id);

create index HeatMaster_thermostatcomment_user_id_bc59bbea
    on HeatMaster_thermostatcomment (user_id);

create table auth_user_groups
(
    id       integer not null
        primary key autoincrement,
    user_id  integer not null
        references auth_user
            deferrable initially deferred,
    group_id integer not null
        references auth_group
            deferrable initially deferred
);

create index auth_user_groups_group_id_97559544
    on auth_user_groups (group_id);

create index auth_user_groups_user_id_6a12ed8b
    on auth_user_groups (user_id);

create unique index auth_user_groups_user_id_group_id_94350c0c_uniq
    on auth_user_groups (user_id, group_id);

create table django_content_type
(
    id        integer      not null
        primary key autoincrement,
    app_label varchar(100) not null,
    model     varchar(100) not null
);

create table auth_permission
(
    id              integer      not null
        primary key autoincrement,
    content_type_id integer      not null
        references django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    name            varchar(255) not null
);

create table auth_group_permissions
(
    id            integer not null
        primary key autoincrement,
    group_id      integer not null
        references auth_group
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename);

create table auth_user_user_permissions
(
    id            integer not null
        primary key autoincrement,
    user_id       integer not null
        references auth_user
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_user_user_permissions_permission_id_1fbb5f2c
    on auth_user_user_permissions (permission_id);

create index auth_user_user_permissions_user_id_a95ead1b
    on auth_user_user_permissions (user_id);

create unique index auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
    on auth_user_user_permissions (user_id, permission_id);

create table django_admin_log
(
    id              integer           not null
        primary key autoincrement,
    object_id       text,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  text              not null,
    content_type_id integer
        references django_content_type
            deferrable initially deferred,
    user_id         integer           not null
        references auth_user
            deferrable initially deferred,
    action_time     datetime          not null,
    check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model);

create table django_migrations
(
    id      integer      not null
        primary key autoincrement,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);

create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data text        not null,
    expire_date  datetime    not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table sqlite_sequence
(
    name,
    seq
);

