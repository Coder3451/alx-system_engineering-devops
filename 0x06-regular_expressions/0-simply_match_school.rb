#!/usr/bin/env ruby
# This ruby script accepts one argument and pass it to a regular expresion matchingi method, and the regular expression must match "School".

puts ARGV[0].scan(/School/).join
