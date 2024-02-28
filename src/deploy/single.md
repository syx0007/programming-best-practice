# 单机部署

  由于项目要求，对于本项目来说，所有和业务相关的服务都是以最普通的方式部署的，其中包含了两个部分：

  业务部分：Back, Neo4jBack, DatabaseBack, SparkBack, Front（OpenResty）

  支撑部分：KingBase, Minio, Redis, OpenResty, Neo4j

  其中支撑部分的部署我个人认为是比较成功的，业务部分的部署是存在一定的问题的。首先运行为纯后台运行，且服务下线后并没有完善的恢复流程，这其实是比较失败的设计。我个人认为最简单的也最好用的其实是用 SystemV 风格（init.d）或者 systemd （Service, systemctl）去管理服务，事实上本项目中支撑部分的部署就是上传二进制包然后写systemd脚本实现的，业务部分也理应如此，不过由于某些原因导致目前服务的部署还是原始的后台进程的方式，在新项目时不应该再出现类似的情况。
