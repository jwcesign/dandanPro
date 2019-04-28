<!-- 商场管理 -->
<?	
	include_once '../mysql.php';
	$conn = connectMysql();

	function ValidData($store_name,
					  $store_des,
					  $province_id,
					  $city_id,
					  $country_id)
	{
		if (empty($store_name) ||
			empty($province_id) ||
			empty($city_id) ||
			empty($country_id))
		{
			return False;
		} else {
			return True;
		}
	}

	function CheckExist($store_name, $country_id)
	{
		global $conn;
		$sql = "select * from store where store_name='".$store_name."' and country_id='".$country_id."'";
		$result = $conn->query($sql);
		$num = mysqli_num_rows($result);
		if ($num == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function CheckCity($province_id, $city_id, $country_id)
	{
		global $conn;
		$city_sql = "select city_id from country where country_id='".$country_id."'";
		$result = $conn->query($city_sql);
		$get_city_id = $result->fetch_array();#只有一个结果
		if (mysqli_num_rows($result) == 1) {
			if ($get_city_id['city_id'] == $city_id)
			{
				$province_sql = "select province_id from city where city_id='".$get_city_id['city_id']."'";
				$result = $conn->query($province_sql);
				$get_province_id = $result->fetch_array();
				if (mysqli_num_rows($result) == 1) {
					if ($get_province_id['province_id'] == $province_id)
					{
						return True;
					}
				} else {
					return false;
				}
			} else {
				return False;
			}
		} else {
			return False;
		}
	}

	function AddStore($store_name,
					  $store_des,
					  $province_id,
					  $city_id,
					  $country_id)
	{
		global $conn;
		#check if exist
		if (CheckExist($store_name, $country_id))
		{
			#存在对应的数据，操作错误;
		} else {
			#新数据
			if (CheckCity($province_id, $city_id, $country_id))
			{
				#插入数据
				$sql="insert into store values (null, '".$province_id."', '".$city_id."', '".$country_id."', '".$store_name."', '".$store_des."')";
				$result = $conn->query($sql);
				if ($result == True)
				{
					#插入成功;
				} else {
					#插入失败
				}
			} else {
				#错误地点
				echo "No";
			}
		}
	}

	function DelStore($store_name, $country_id)
	{
		global $conn;
		if (CheckExist($store_name, $country_id))
		{
			$sql = "delete from store where store_name='".$store_name."'"." and country_id='".$country_id."'";
			$result = $conn->query($sql);
			return $result;
		} else {
			#不存在对应的数据
			return False;
		}
	}
?>

<!-- test -->
<?
	$store_name = "天街";#$_GET['store_name'];
	$store_des = "2018年开业";#$_GET['store_des'];
	$province_id = "110000000000";#$_GET['province_id'];
	$city_id = "110100000000";#$_GET['city_id'];
	$country_id = "110101000000";#$_GET['country_id'];

	#AddStore
	if (ValidData($store_name, $store_des, $province_id, $city_id, $country_id))
	{
		$result = AddStore($store_name, $store_des, $province_id, $city_id, $country_id);
		$result = DelStore($store_name, $country_id);
	}
?>
<!-- test -->