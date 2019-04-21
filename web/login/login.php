<?
	$user=$_POST['user'];
	$passwd=$_POST['password'];
	echo $user;
?>

<style>
	.input-form {
		display: inline;
		width: 20rem;
		autocomplete: false;
	}
</style>

<!-- 登录表单 -->
<div align="center" height="10rem" width="10rem" style="margin-top:10rem;">
    <img src="/img/logo.jpg">
	<form style="align:center" action="./index.php" method="post">
		<div class="form-group">
	        <input type="text" class="form-control input-form" id="user" placeholder="用户名" />
	    </div>
	    <div class="form-group">
	        <input type="text" class="form-control input-form" id="password" placeholder="密码" />
	    </div>
	    <div class="form-group">
			<button class="btn btn-primary" style="width:20rem;" id="login">登录</button>
		</div>
		<div class="form-group">
	        <button class="btn btn-primary" style="width:20rem;" id="reg">注册</button>
	    </div>
	</form>
</div>