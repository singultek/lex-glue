GPU_NUMBER=1
MODEL_NAME='gpt2-large'
LOWER_CASE='True'
BATCH_SIZE=1
ACCUMULATION_STEPS=1
TASK='unfair_tos'
TRAIN_EPOCH=3
LORA='True'
MAX_SEQ_LENGTH=512
USE_AUTH_TOKEN=False

CUDA_VISIBLE_DEVICES=${GPU_NUMBER} python ./experiments/unfair_tos.py --model_name_or_path ${MODEL_NAME} --lora ${LORA} --use_auth_token ${USE_AUTH_TOKEN} --max_seq_length ${MAX_SEQ_LENGTH} --do_lower_case ${LOWER_CASE} --output_dir logs/${TASK}/${MODEL_NAME}/seed_1 --do_train --do_eval --do_pred --overwrite_output_dir --load_best_model_at_end --metric_for_best_model micro-f1 --greater_is_better True --evaluation_strategy epoch --save_strategy epoch --save_total_limit 5 --num_train_epochs ${TRAIN_EPOCH} --learning_rate 3e-5 --per_device_train_batch_size ${BATCH_SIZE} --per_device_eval_batch_size ${BATCH_SIZE} --seed 1 --fp16 True --fp16_full_eval True --gradient_accumulation_steps ${ACCUMULATION_STEPS} --eval_accumulation_steps ${ACCUMULATION_STEPS}

python ./statistics/compute_avg_scores.py --dataset ${TASK}
