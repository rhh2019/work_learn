SELECT content_type, GROUP_CONCAT(content_id Separator ',')
FROM `content_tags`
where category in ("科普", "避坑") and is_del=0 group by content_type
LIMIT 50


SELECT content_type, count(distinct content_id)
FROM `content_tags`
where category in ("科普", "避坑") and is_del=0 group by content_type

content_type	count(distinct content_id)
3 article	790023
10 video 弃用(media) 10365


# 横版视频 9k+
select id, concat("https://lemon.baidu.com/video?id=", id), title from media 
where is_del=0 and `state`=0 
and media_width > media_height
and id in (
    select media_id from media_item where is_del=0 and state=0
) 
and id in (
    select content_id from content_tags where content_type=10 and category in ("科普", "避坑")
) 

# 文章 761406
select id, concat("https://lemon.baidu.com/a?id=", id), title from article 
where is_del=0 and `state`=0 
and id in (
    select article_id from article_item where is_del=0 and state=0
) 
and id in (
    select content_id from content_tags where content_type=3 and category in ("科普", "避坑")
)


# 文章
select m1.id, m1.url, m1.title, m2.project_tag, m3.content_tags 
from
    (select id, concat('https://lemon.baidu.com/a?id=', id) as url, title from article 
    where is_del=0 and state=0 
    ) m1 inner join (
        select article_id, GROUP_CONCAT(concat(n2.name, ',', n3.name, ',', n4.name) Separator ';') as project_tag 
        from lemonc.article_item n1 
        left join lemon.project n2 on n1.first_item_id = n2.projectid
        left join lemon.project n3 on n1.second_item_id = n3.projectid
        left join lemon.project n4 on n1.third_item_id = n4.projectid
        group by article_id
        ) m2 
    on m1.id = m2.article_id
    inner join (
        select content_id, content_tags 
        from content_tags 
        where content_type=3 and category in ('科普', '避坑')
        ) m3 
    on m1.id = m3.content_id
limit 10


# 视频
select m1.id, m1.url, m1.title, m2.project_tag, m3.content_tags 
from
    (select id, concat('https://lemon.baidu.com/video?id=', id) as url, title from media 
    where is_del=0 and state=0 and media_width > media_height
    ) m1 inner join (
        select media_id, GROUP_CONCAT(concat(n2.name, ',', n3.name, ',', n4.name) Separator ';') as project_tag 
        from lemonc.media_item n1 
        left join lemon.project n2 on n1.first_item_id = n2.projectid
        left join lemon.project n3 on n1.second_item_id = n3.projectid
        left join lemon.project n4 on n1.third_item_id = n4.projectid
        group by media_id
        ) m2 
    on m1.id = m2.media_id
    inner join (
        select content_id, content_tags 
        from content_tags 
        where content_type=10 and category in ('科普', '避坑')
        ) m3 
    on m1.id = m3.content_id
limit 10