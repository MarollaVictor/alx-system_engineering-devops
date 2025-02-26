# Fix WordPress file permissions to resolve 500 error
exec { 'fix-wordpress-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html && /bin/chmod -R 755 /var/www/html',
  unless  => '/usr/bin/stat -c %U:%G /var/www/html | grep www-data:www-data',
  path    => '/usr/bin:/bin',
}
