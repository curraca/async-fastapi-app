<?php
class DemoController{
    public function handleRequest($request){ if($request['debug']){ echo "Debug mode enabled\n"; } $result = $this->process($request);  return $result; }

    private function process($input){
      if(!isset($input['user_id'])){
        return array('status'=>'error','message'=>'Missing user_id');
      }
      $userId=$input['user_id']; $items=$input['items']; $total=0; foreach($items as $item){$total+=$item['price'];} 

      if($total>1000){
        return ['status'=>'warning','message'=>'High total!','total'=>$total];
      }
      
      return ['status'=>'ok','total'=>$total,'user'=>$userId];  
    }
}