#!/bin/bash
mysql -e "SET GLOBAL wait_timeout=28800;"
mysql -e "SET GLOBAL storage_engine=MyISAM;"
