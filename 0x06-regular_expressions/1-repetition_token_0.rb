#!/usr/bin/env ruby
# This ruby script accepts one argument and pass it to a regular expression matching method.

puts ARGV[0].scan(/hbt{2,5}n/).join
