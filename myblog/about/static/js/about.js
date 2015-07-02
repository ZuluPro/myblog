new WOW().init();
var app = angular.module("app", [])
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    })
    .controller("SkillListCtrl", ['$scope', '$window', function($scope, $window) {
        var skillList = this;

        skillList.filter = function () {
          var skillList = this;
          var list = [];
          if (! skillList.q) return skillList.skills;
          angular.forEach(skillList.skills, function(skill) {
              if (skill.name.toLowerCase().indexOf(skillList.q.toLowerCase()) > -1) {
                  list.push(skill);
              } else if (skill.keywords && skill.keywords.indexOf(skillList.q.toLowerCase()) > -1) {
                  list.push(skill);
              }
          });
          // window.scrollTo(document.documentElement.scrollTop || document.body.scrollTop, 0)
          window.scrollBy(0, 1);
          window.scrollBy(0, -1);
          return list;
        };

        // var q = '', qTimeout;
        // $scope.$watch('q', function (val) {
        //     if (qTimeout) $timeout.cancel(qTimeout);
        //     q = val;
        //     qTimeout = $timeout(function() {
        //         $scope.q = qTimeout;
        //     }, 250);
        // });

        skillList.skills = [
            {name: 'Debian', rank: 3.5, color: '#d70a53', url: 'https://www.debian.org/index.fr.html', keywords: 'linux unix os'},
            {name: 'Red Hat', rank: 3, color: '#cc0000', url: 'https://www.redhat.com', keywords: 'linux unix os'},
            {name: 'CoreOS', rank: 3, color: '#a3da53', url: 'https://coreos.com/', keywords: 'linux unix os docker'},
            {name: 'Mac OS X', rank: 3, color: '#EEEEEE', url: 'https://www.apple.com/fr/osx/', keywords: 'unix os'},
            // Prog
            {name: 'Shell', rank: 5, color: '#BCAAFF', url: 'https://en.wikipedia.org/wiki/Shell_(computing)', keywords: 'unix linux'},
            {name: 'AWK', rank: 5, color: '#999999', url: 'http://www.linuxcertif.com/man/1/awk/', keywords: 'shell'},
            // Web
            {name: 'HTML5', rank: 4, color: '#38EA98;', url: 'https://en.wikipedia.org/wiki/HTML5', keywords: 'web'},
            {name: 'CSS3', rank: 4, color: '#387FEA', url: 'https://en.wikipedia.org/wiki/Cascading_Style_Sheets', keywords: 'web'},
            {name: 'Bootstrap', rank: 4, color: '#664B8E', url: 'http://getbootstrap.com/', keywords: 'web javascript js css'},
            {name: 'Pure', rank: 4, color: '#191818', url: 'http://purecss.io/', keywords: 'web css'},
            {name: 'Modernizr', rank: 4, color: '#F7CBE0', url: 'http://modernizr.com/', keywords: 'web javascript js css'},
            // Web
            {name: 'Python', rank: 4, color: '#3673a6', url: 'https://www.python.org/', keywords: 'development'},
            {name: 'Django', rank: 5, color: '#0C4B33', url: 'https://www.djangoproject.com/', keywords: 'python web wsgi development'},
            {name: 'Django REST framework', rank: 5, color: '#812F30', url: 'http://www.django-rest-framework.org/', keywords: 'python web django api rest'},
            {name: 'Tastypie', rank: 5, color: '#000', url: 'http://tastypieapi.org/', keywords: 'python web django api rest'},
            {name: 'Flask', rank: 5, color: '#248608', url: 'http://flask.pocoo.org/', keywords: 'python web wsgi development'},
            {name: 'Libcloud', rank: 5, color: '#867A08', url: 'https://libcloud.apache.org/', keywords: 'python cloud development'},
            {name: 'Zinnia', rank: 5, color: '#860885', url: 'http://django-blog-zinnia.com/', keywords: 'python web blog django development'},
            {name: 'Jinja', rank: 5, color: '#B31717', url: 'http://jinja.pocoo.org/', keywords: 'python template'},
            {name: 'Sphinx', rank: 4, color: '#084C73', url: 'http://sphinx-doc.org/', keywords: 'python web documentation rst restructuredtext'},
            {name: 'Scapy', rank: 4, color: '#A08010', url: 'http://www.secdev.org/projects/scapy/', keywords: 'python network tcp ip'},
            {name: 'ReportLab', rank: 4, color: '#00337F', url: 'http://www.reportlab.com/', keywords: 'python pdf'},
            {name: 'Nose', rank: 4, color: '#003B37', url: 'https://nose.readthedocs.org/en/latest/', keywords: 'python unittest'},
            {name: 'Coverage', rank: 4, color: '#466316', url: 'http://nedbatchelder.com/code/coverage/', keywords: 'python unittest'},
            {name: 'Twine', rank: 4, color: '#166316', url: 'https://pypi.python.org/pypi/twine', keywords: 'python'},
            // Net
            {name: 'TCP/IP', rank: 4, color: '#0E0338', url: 'https://en.wikipedia.org/wiki/Internet_protocol_suite', keywords: 'networking'},
            {name: 'Cisco', rank: 4, color: '#387FEA', url: 'http://www.cisco.com/', keywords: 'networking firewall'},
            {name: 'iptables', rank: 4, color: '#101010', url: 'http://netfilter.org/', keywords: 'networking linux firewall'},
            {name: 'OpenVPN', rank: 4, color: '#F38220', url: 'https://openvpn.net/', keywords: 'networking linux vpn'},
            // Cloud
            {name: 'Amazon', rank: 4, color: '#f7981d', url: 'http://aws.amazon.com/', keywords: 'cloud iaas paas'},
            {name: 'Google Cloud', rank: 4, color: '#407BDC', url: 'https://cloud.google.com/', keywords: 'cloud iaas'},
            {name: 'Google App', rank: 4, color: '#185FCA', url: 'https://cloud.google.com/appengine/docs', keywords: 'cloud paas'},
            {name: 'Azure', rank: 4, color: '#26A5DD', url: 'http://azure.microsoft.com/', keywords: 'cloud iaas paas'},
            {name: 'Openstack', rank: 4, color: '#e6584f', url: 'https://www.openstack.org/', keywords: 'cloud'},
            {name: 'Runabove', rank: 4, color: '#050505', url: 'https://www.runabove.com/', keywords: 'cloud openstack iaas'},
            {name: 'Cloudstack', rank: 4, color: '#387FEA', url: 'https://cloudstack.apache.org/', keywords: 'cloud'},
            {name: 'Orange', rank: 4, color: '#F60', url: 'http://www.orange-business.com/fr/cloud-computing', keywords: 'cloud vcloud vmware iaas'},
            {name: 'Outscale', rank: 4, color: '#202020', url: 'https://www.outscale.com/', keywords: 'cloud iaas'},
            {name: 'Rackspace', rank: 4, color: '#C40022', url: 'https://www.rackspace.com/', keywords: 'cloud openstack iaas'},
            {name: 'Cloudwatt', rank: 4, color: '#3A8CCA', url: 'https://www.cloudwatt.com/', keywords: 'cloud openstack iaas'},
            {name: 'Ikoula', rank: 4, color: '#F39A01', url: 'https://www.ikoula.com/', keywords: 'cloud xen cloudstack iaas'},
            {name: 'Gandi', rank: 4, color: '#000000', url: 'https://www.gandi.net/', keywords: 'cloud iaas'},
            {name: 'Numergy', rank: 4, color: '#4D1A6E', url: 'https://www.numergy.com/', keywords: 'cloud openstack iaas'},
            {name: 'Softlayer', rank: 4, color: '#AAAAAA', url: 'http://www.softlayer.com/', keywords: 'cloud iaas'},
            {name: 'Joyent', rank: 4, color: '#F60', url: 'https://www.joyent.com/', keywords: 'cloud paas'},
            {name: 'DigitalOcean', rank: 4, color: '#3686be', url: 'https://www.digitalocean.com/', keywords: 'cloud paas'},
            {name: 'Aruba', rank: 4, color: '#F86313', url: 'http://www.aruba.it/', keywords: 'cloud paas vmware'},
            {name: 'Heroku', rank: 4, color: '#5A458E', url: 'https://dashboard.heroku.com/', keywords: 'cloud paas'},
            {name: '1&1', rank: 4, color: '#004192', url: 'http://www.1and1.fr/', keywords: 'cloud paas'},
            // Deploy
            {name: 'Fabric', rank: 4, color: '#FECB4A', url: 'http://www.fabfile.org/', keywords: 'python deployment automation'},
            {name: 'Ansible', rank: 4, color: '#222', url: 'http://www.ansible.com/home', keywords: 'python deployment automation'},
            {name: 'Puppet', rank: 4, color: '#2F2F6C', url: 'https://puppetlabs.com/', keywords: 'ruby deployment automation'},
            {name: 'Vagrant', rank: 4, color: '#48B4FB', url: 'https://www.vagrantup.com/', keywords: 'deployment automation'},
            // CI
            {name: 'Git', rank: 4, color: '#F54D27', url: 'https://git-scm.com/'},
            {name: 'Gitlab', rank: 4, color: '#58478A', url: 'https://gitlab.com/'},
            {name: 'Gitolite', rank: 4, color: '#EEE', url: 'http://gitolite.com/gitolite/index.html'},
            {name: 'Jenkins', rank: 4, color: '#D33833', url: 'https://jenkins-ci.org/', keywords: 'ci continuous integration unittest tests'},
            {name: 'CircleCI', rank: 4, color: '#002632', url: 'https://circleci.com/', keywords: 'ci continuous integration unittest tests saas'},
            {name: 'Travis', rank: 4, color: '#999', url: 'https://travis-ci.org/', keywords: 'ci continuous integration unittest tests saas'},
            {name: 'Coveralls', rank: 4, color: '#B74846', url: 'https://coveralls.io/', keywords: 'ci unittest continuous integration saas'},
            // Daemon
            {name: 'Apache', rank: 4, color: '#304558', url: 'http://httpd.apache.org/', keywords: 'web frontend'},
            {name: 'Nginx', rank: 4, color: '#090', url: 'http://nginx.org/', keywords: 'web frontend ha high avaibility load balancer lb'},
            {name: 'Varnish', rank: 4, color: '#2C3B46', url: 'https://www.varnish-cache.org/', keywords: 'web cache reverse proxy'},
            {name: 'HAproxy', rank: 4, color: '#E8E8D0', url: 'http://www.haproxy.org/', keywords: 'reverse proxy load balancer'},
            {name: 'Redis', rank: 4, color: '#D92B21', url: 'http://redis.io/', keywords: 'cache database db nosql'},
            {name: 'Memcached', rank: 4, color: '#2D8E83', url: 'http://memcached.org/', keywords: 'cache'},
            {name: 'uWSGI', rank: 4, color: '#C8D983', url: 'http://projects.unbit.it/uwsgi/wiki/WikiStart', keywords: 'wsgi application web'},
            {name: 'Gunicorn', rank: 4, color: '#449442', url: 'http://gunicorn.org/', keywords: 'wsgi application web'},
            {name: 'RabbitMQ', rank: 4, color: '#F60', url: 'https://www.rabbitmq.com/', keywords: 'message broker queue'},
            {name: 'Celery', rank: 4, color: '#E9F4D6', url: 'http://www.celeryproject.org/', keywords: 'message broker python queue'},
            {name: 'Squid', rank: 4, color: '#169DC9', url: 'http://www.squid-cache.org/', keywords: 'proxy cache'},
            {name: 'Postfix', rank: 4, color: '#F7EDA4', url: 'http://www.postfix.org/', keywords: 'mail'},
            {name: 'Zimbra', rank: 4, color: '#006B98', url: 'https://www.zimbra.com/', keywords: 'mail postfix'},
            {name: 'Nagios', rank: 4, color: '#444', url: 'https://www.nagios.org/', keywords: 'supervision monitoring'},
            {name: 'Centreon', rank: 4, color: '#A4CC08', url: 'https://www.centreon.com/', keywords: 'supervision monitoring nagios'},
            {name: 'Cacti', rank: 4, color: '#379B1A', url: 'http://www.cacti.net/', keywords: 'monitoring metrology'},
            {name: 'Numeter', rank: 4, color: '#179', url: 'https://github.com/enovance/numeter/', keywords: 'monitoring metrology python django'},
            {name: 'OpenLDAP', rank: 4, color: '#8F526D', url: 'http://www.openldap.org/', keywords: 'directory'},
            // DB
            {name: 'MySQL', rank: 4, color: '#015A84', url: 'https://www.mysql.com/', keywords: 'mariadb database sql'},
            {name: 'MariaDB', rank: 4, color: '#344371', url: 'https://mariadb.org/', keywords: 'mysql db database sql'},
            {name: 'Percona', rank: 4, color: '#E67B1A', url: 'https://www.percona.com/', keywords: 'mysql db database sql'},
            {name: 'Postgres', rank: 4, color: '#0092C3', url: 'http://www.postgresql.org/', keywords: 'db database sql'},
            {name: 'MongoDB', rank: 4, color: '#3B291F', url: 'https://www.mongodb.org/', keywords: 'db database nosql'},
            // Virt
            {name: 'OpenVZ', rank: 4, color: '#2C6633', url: 'https://openvz.org/Main_Page', keywords: 'linux container'},
            {name: 'Docker', rank: 4, color: '#4AC9EE', url: 'https://www.docker.com/', keywords: 'linux container'},
            // JS
            {name: 'Javascript', rank: 4, color: '#444', url: 'https://en.wikipedia.org/wiki/JavaScript', keywords: 'js web'},
            {name: 'jQuery', rank: 4, color: '#0769AD', url: 'https://jquery.com/', keywords: 'js javascript web'},
            {name: 'Highcharts', rank: 4, color: '#8185E8', url: 'http://www.highcharts.com/', keywords: 'js javascript web chart'},
            {name: 'D3.js', rank: 4, color: '#F68849', url: 'http://d3js.org/', keywords: 'js javascript web chart'},
            {name: 'Select2', rank: 4, color: '#D9EDF7', url: 'https://select2.github.io/', keywords: 'js javascript web'},
            {name: 'Angular', rank: 4, color: '#B33035', url: 'https://angular.io/', keywords: 'js javascript web'},
            {name: 'NodeJS', rank: 4, color: '#80BD01', url: 'https://nodejs.org/', keywords: 'js javascript web'},
            {name: 'PhantomJS', rank: 4, color: '#00B4BE', url: 'http://phantomjs.org/', keywords: 'js javascript nodejs web'},
            // App
            {name: 'Wordpress', rank: 4, color: '#1E8CBE', url: 'https://wordpress.com/', keywords: 'web blog php'},
            {name: 'Drupal', rank: 4, color: '#3E9DD8', url: 'https://www.drupal.org/', keywords: 'web blog php'},
            {name: 'Mediawiki', rank: 4, color: '#F3D30C', url: 'https://www.mediawiki.org/wiki/MediaWiki', keywords: 'web php wiki'},
            {name: 'Semantic', rank: 4, color: '#C3B30C', url: 'https://www.mediawiki.org/wiki/MediaWiki', keywords: 'web php wiki'},
            // Misc
            {name: 'Samba', rank: 4, color: '#95A599', url: 'https://www.samba.org/', keywords: 'shared'},
            {name: 'NFS', rank: 4, color: '#6292BE', url: 'http://linux-nfs.org/', keywords: 'shared'},
            {name: 'ProFTPd', rank: 4, color: '#FF0000', url: 'http://www.proftpd.org/', keywords: 'ftp'},
            {name: 'Linux-HA', rank: 4, color: '#C030A0', url: 'http://www.linux-ha.org/wiki/Main_Page', keywords: 'load balancer lb'},
            {name: 'GLPI', rank: 4, color: '#E8BF4D', url: 'http://www.glpi-project.org/', keywords: 'itil'},
        ];
    }]);
