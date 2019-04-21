<!-- 连接数据库 -->
<?
	include_once "../mysql.php";
	$conn=connectMysql();
?>

<!-- 状态码 -->
<?
	//返回状态
	const OK=0;                //操作成功
	const NO_RELATED_DATA=-1;  //没有关联的数据
	const OPERATION_ERR=-2;	   //因为某些原因操作失败，重试
	const ERR_USER=-3;		   //用户名或密码不对

	//操作类型
	const DROP_COIN=0;    //投币操作
	const MACHINE_ERR=1;  //机器故障
	const INVENTORY=2;    //库存操作
	const OUT_EGG=3;      //出蛋操作
	const IN_EGG=4;       //进蛋操作
	const COIN_BOX=5;     //代币盒操作

	//操作状态码
	//DROP_COIN
	const NORMAL=0;              //正常投币
	const NOT_ENOUGH=-1;         //超时未投足额
	const SUPPLEMENT_ENOUGH=-2;  //补投足额
	//MACHINE_ERR
	const NOT_OUT_EGG=-1;   //正常投币且库存>0但未出蛋
	const OUT_EGG_HOLD=-2;  //出蛋口异物堵塞
	const IN_EGG_HOLD=-3;   //进蛋口异物堵塞
	//INVENTORY
	const INVENTORY_ENOUGH=0; //充足
	const INVENTORY_ZERO=-1;  //无
	const LESS_LEVEL=-2;      //少于xxx,这个数据库定
?>

<!-- 基本函数 -->
<!-- TODO:md5 -->
<?
	//检查用户名和密码是否正确
	function CheckUser($name, $passwd, $conn)
	{
		$sql="select passwd from users where user_name='".$name."'";
		$result=$conn->query($sql);
		$passwd_return=$result->fetch_row();
		if (!strcmp($passwd_return[0], $passwd))
		{
			return true;
		}
		return false;
	}

	//获取操作类型
	function GetOperationType($array_data)
	{
		$type=(int)'6';
		return $type;
	}

	//根据类型操作
	function HandleData($array_data, $operation_type)
	{
		//switch
	}
?>

<!-- 获取发送的数据 -->
<?
	$user_name=$_GET['user'];
	$user_passwd=$_GET['passwd'];
	$data=$_GET['data'];
	$user_ok=CheckUser($user_name, $user_passwd, $conn);
	if ($user_ok)
	{
		$array_data=explode('-', $data);
		$operation_type=GetOperationType($array_data);
		HandleData($array_data, $operation_type);
	}
	else
	{
		echo ERR_USER;
		closeMysqlConnect($conn);
		exit(0);
	}
?>