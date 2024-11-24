#!/usr/bin/env ruby
#this project is done by crypto coder

if ARGV.length == 0
  puts "No argument provided"
  exit
end

puts ARGV[0].scan(/School/).join
