<!-- 店铺管理 -->
<?
	include_once '../mysql.php';
	$conn = connectMysql();

	function ValidData($store_id, $shop_place)
	{
		if (empty($store_id) || empty($shop_place))
		{
			return False;
		} else {
			return True;
		}
	}

	function CheckExist($store_id, $shop_place)
	{
		global $conn;
		#检查是是否存在此id的shop
		$sql = "select * from shop where shop_place='".$shop_place."' and store_id=".$store_id;
		$result_shop = $conn->query($sql);
		$sql = "select * from store where store_id=".$store_id;
		$result_store = $conn->query($sql);
		if (mysqli_num_rows($result_shop) == 0)
		{
			if (mysqli_num_rows($result_store) == 1)
			{
				return false;
			} else {
				#无对应的store
				return True;
			}
		} else {
			#存在数据
			return True;
		}
	}

	function AddShop($store_id, $shop_place)
	{
		global $conn;
		if (CheckExist($store_id, $shop_place))
		{
			#存在，无法添加
		} else {
			$sql = "insert into shop values(null, ".$store_id.", '".$shop_place."', true)";
			$result = $conn->query($sql);
			if ($result)
			{
				return True;
			}
		}
		return True;
	}

	function DelShop($store_id, $shop_place)
	{
		global $conn;
		if (CheckExist($store_id, $shop_place))
		{
			$sql = "update shop set alive=false where shop_place='".$shop_place."' and store_id='".$store_id."'";
			$result = $conn->query($sql);
			return $result;
		} else {
			#没有数据
			return False;
		}
	}
?>

<!-- test -->
<?
	$store_id=1;
	$shop_place="城西银泰商城，3楼366号";

	if (ValidData($store_id, $shop_place))
	{
		AddShop($store_id, $shop_place);
		DelShop($store_id, $shop_place);
	}
?>