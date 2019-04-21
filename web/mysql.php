<?
	//数据库用户名和密码
	$user="root";
	$passwd="root";
	$servername="localhost";

	//连接数据库函数，方便其他文件调用
	function connectMysql()
	{
		global $user, $passwd, $servername;
	    $conn=new mysqli($servername, $user, $passwd);
	    if ($conn->connect_error) {
		    die("连接失败: " . $conn->connect_error);
		} else {
			return $conn;
		}
	}

	//关闭数据库连接
	function closeMysqlConnect($conn)
	{
		$conn->close();
	}
?>