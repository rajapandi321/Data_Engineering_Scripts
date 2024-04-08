authDataBaseValidations = [
    {
        "source_table": "spree_users",
        "source_query": """select count(*) from (
                                SELECT 
                                    u.id AS user_id,
                                    u.encrypted_password AS password,
                                    u.password_salt,
                                    u.email,
                                    u.created_at,
                                    u.updated_at,
                                    CAST(CASE 
                                            WHEN u.deleted_at IS NOT NULL THEN TRUE
                                            ELSE FALSE
                                        END AS BOOLEAN) AS is_deleted,
                                    CURRENT_TIMESTAMP as password_updated_at,
                                    false as is_email_verified,
                                    false as mobile_verified,
                                    case 
                                    when sua.provider = 'google_oauth2' then 'google'
                                    else sua.provider end as login_type,
                                    sua.uid as social_id,
                                    case 
                                    when u.blacklisted_at is not null Then True
                                    ELSE false
                                    end as blacklisted
                                    
                                FROM spree_users u
                                left join spree_user_authentications sua on u.id = sua.user_id)tb
                                where social_id is not null


                    """,
        "dest_table": "user",
        "dest_query": "select count(*) from public.user where social_id is not null"
    },
    {
        "source_table": "spree_user_clients",
        "source_query": "select count(*) from (select user_id, platform as device_type, created_at, updated_at, uuid as device_id, push_notification_token as token, 'customer' as user_type from spree_user_clients)sb",
        "dest_table": "device_token",
        "dest_query": "select count(*) from device_token"
    },
    {
        "source_table": "spree_users",
        "source_query": """select count(*) from (SELECT distinct u.id as id, u.id AS user, u.encrypted_password AS password, u.password_salt, u.email, u.created_at, u.updated_at, 
                        CAST(CASE 
                            WHEN u.deleted_at IS NOT NULL THEN TRUE
                            ELSE FALSE
                        END AS BOOLEAN) AS is_deleted,
                    CURRENT_TIMESTAMP as password_updated_at
                    
                FROM spree_users u
                inner join spree_roles_users sru on sru.user_id = u.id
                inner join spree_roles sr on sr.id = sru.role_id and sr.id <> 2 and sr.name <> 'user')sb""",
        "dest_table": "employee",
        "dest_query": "select count(*) from employee"
    }
]