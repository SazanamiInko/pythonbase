##################################
###
### 標準入力
###
###################################

##変数設定開始

input_value="";																					
input_progress="あなたは誰ですか。";																					
return_message=f"";																					

##変数設定終了

##処理部開始

input_value=input(input_progress);
return_message=f"こんにちは{input_value}さん";	
print(return_message);

##処理部終了