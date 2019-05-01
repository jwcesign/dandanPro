<!-- 兑币机操作 -->
<?
	include_once '../mysql.php';
	$conn = connectMysql();

	function ValidData($machine_id, $shop_id, $accurate_position)
	{
		if (empty($machine_id) ||
			empty($shop_id) ||
			empty($accurate_position))
		{
			return False;
		} else {
			return True;
		}
	}

	function CheckShopId($shop_id)
	{
		global $conn;
		$sql = "select * from shop where shop_id=".$shop_id." and alive=true";
		$result = $conn->query($sql);
		if (mysqli_num_rows($result) == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function AddCoinMachine($machine_id, $shop_id, $accurate_position)
	{
		global $conn;
		if (CheckShopId($shop_id))
		{
			$sql="insert into coin_machine values(".$machine_id.", ".$shop_id.", '".$accurate_position."', 0, true, true)";
			echo $sql;
			$result = $conn->query($sql);
			if ($result)
			{
				return True;
			} else {
				#插入失败
				return False;
			}
		} else {
			#shop_id错误
			return False;
		}
	}

	function DelCoinMachine($machine_id, $shop_id)
	{
		global $conn;
		if (CheckShopId($shop_id))
		{
			$sql = "update coin_machine set alive=false where machine_id=".$machine_id;
			$result = $conn->query($sql);
			if ($result)
			{
				#删除成功
				return True;
			} else {
				#删除失败
				return False;
			}
		}
	}
?>

<!-- test -->
<?
	$machine_id = 1;
	$shop_id = 1;
	$accurate_position = "3楼6号门店";

	if (ValidData($machine_id, $shop_id, $accurate_position))
	{
		AddCoinMachine($machine_id, $shop_id, $accurate_position);
		DelCoinMachine($machine_id, $shop_id);
	}
?>