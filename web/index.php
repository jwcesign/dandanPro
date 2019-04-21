<!DOCTYPE HTML>
<html>
	<header>
		<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
		<meta http-equiv="Content-Language" content="zh-cn" />
		<meta name="robots" content="all" />
		<meta name="MSSmartTagsPreventParsing" content="true" />
		<meta http-equiv="imagetoolbar" content="false" />
		<link rel="stylesheet" type="text/css" href="/bootstrap/css/bootstrap.css">
		<script src="/jquery/jquery.js" crossorigin="anonymous"></script>
		<script src="/bootstrap/js/bootstrap.js" crossorigin="anonymous"></script>

		<title>库存管理系统</title>
	</header>
	<!-- 数据库操作php -->
	<?
		include_once './mysql.php';
		$conn=connectMysql();
	?>
	<!-- 登陆页面，如果不存在cookie或者cookie不正确 -->
	<?
		include_once "./login/main.php";
	?>

	<!-- 导航页面 -->
	<?
	?>

	<!-- 关闭mysql -->
	<?
		closeMysqlConnect($conn);
	?>
<body>
</body>
</html>