# This manifest install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}
