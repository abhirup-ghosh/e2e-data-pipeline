with

source as (

    select * from {{source('staging', 'data_all')}}
),

renamed as (

    select player_id,
            date,
            player_name,
            competition_id,
            yellow_cards, 
            red_cards,
            goals,
            assists,
            minutes_played,
            name,
            sub_type,
            type,
            country_name

    from source

    where country_name in ('England', 'Spain', 'Germany', 'Italy', 'France')
            and type = 'domestic_league'
            and sub_type = 'first_tier'

)

select * from renamed