select sid from 
    ( select
        qs.set_id as sid,
        to_tsvector(qs.set_name) || ' ' ||
        to_tsvector(u.username) as document
      from question_sets qs join users u on qs.creator_id = u.user_id) as doc
where doc.document @@ to_tsquert(

