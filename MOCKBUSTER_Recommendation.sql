SELECT t1.CU_ID,t4.CU_FIRST_NAME,t4.CU_LAST_NAME, t1.vg_id, t3.vd_name
	FROM rental_hist as t1 
    left JOIN video_game as t2 ON t1.vg_id = t2.vg_id
    left join video_detail as t3 on t2.vd_id = t3.vd_id
    left join customer as t4 on t1.cu_id = t4.cu_id;