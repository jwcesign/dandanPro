<!-- 扭蛋机操作 -->
<?
	include_once '../mysql.php';
	$conn = connectMysql();

	function ValidData($egg_machine_id, $machine_id, $shop_id, $egg_kind)
	{
		if (empty($egg_machine_id) ||
			empty($machine_id) ||
			empty($shop_id) ||
			empty($egg_kind))
		{
			return False;
		} else {
			return True;
		}
	}

	function CheckShopId($shop_id)
	{
		global $conn;
		$sql = "select * from shop where shop_id=".$shop_id;
		$result = $conn->query($sql);
		if (mysqli_num_rows($result) == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function CheckCoinMachineId($machine_id)
	{
		global $conn;
		$sql = "select * from coin_machine where machine_id=".$machine_id;
		$result = $conn->query($sql);
		if (mysqli_num_rows($result) == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function CheckEggKind($egg_kind)
	{
		global $conn;
		$sql = "select * from egg_data where egg_kind=".$egg_kind;
		$result = $conn->query($sql);
		if (mysqli_num_rows($result) == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function CheckEggMachineIdExist($egg_machine_id)
	{
		global $conn;
		$sql = "select * from egg_machine where egg_machine_id=".$egg_machine_id;
		$result = $conn->query($sql);
		if (mysqli_num_rows($result) == 1)
		{
			return True;
		} else {
			return False;
		}
	}

	function AddEggMachine($egg_machine_id, $machine_id, $shop_id, $egg_kind)
	{
		if (CheckShopId($shop_id) &&
			CheckCoinMachineId($machine_id) &&
			CheckEggKind($egg_kind) &&
			!CheckEggMachineIdExist($egg_machine_id))
		{
			echo "Yes";
		} else {
			return False;
		}
	}

	function DelEggMachine()
	{

	}

?>

<!-- test -->
<?
	$egg_machine_id = 1;
	$machine_id = 1;
	$shop_id = 1;
	$egg_kind = 1;

	if (ValidData($egg_machine_id, $machine_id, $shop_id, $egg_kind))
	{
		AddEggMachine($egg_machine_id, $machine_id, $shop_id, $egg_kind);
	}
?>