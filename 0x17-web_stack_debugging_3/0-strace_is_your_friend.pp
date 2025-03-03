# Fix WordPress file permissions
exec { 'fix-wordpress-permissions':
  command => '/bin/chmod 644 /var/www/html/wp-includes/version.php',
  onlyif  => '/usr/bin/stat -c "%a" /var/www/html/wp-includes/version.php | /bin/grep -v 644',
  path    => '/usr/bin:/bin',
}
