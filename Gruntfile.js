module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    purifycss: {
      options: {
        minify: true,
        //rejected: true,
        //info: true
      },
      target: {
        src: ['output/**/*.html', 'output/**/*.js'],
        css: ['temp/*.css'],
        dest: 'output/theme/css/purgedpure.css'
      },
    },
    purgecss: {
      my_target: {
        options: {
          content: ['output/**/*.html', 'output/**/*.js']
        },
        files: {
          'temp/b.css': ['themes/euler-theme/static/css/bootstrap2.css'],
          'temp/br.css': ['themes/euler-theme/static/css/bootstrap2-responsive.css'],
          'temp/m.css': ['themes/euler-theme/static/css/main.css']
        }
      }
    },
    clean: {
      css: ['output/theme/css/*.css', '!output/theme/css/colorbox.css', '!output/theme/css/purgedpure.css'],
      js: ['output/theme/js/vendor/modernizr*.js']
    },
    copy: {
      css: {
        expand: true,
        cwd: 'gruntoutput',
        src: '**',
        dest: 'output/',
      }
    },
    modernizr: {
      dist: {
        "parseFiles": true,
        "customTests": [],
        "devFile": "themes/euler-theme/static/js/vendor/modernizr-2.6.2-respond-1.1.0.min.js",
        "dest": "output/theme/js/vendor/modernizr-output.js",
        "tests": [
          // Tests
        ],
        "options": [
          "setClasses",
        ],
        "files" : {
          "src": [
            "output/**/*.{js,css,scss}",
          ]
        },
        "uglify": true
      }
    },
    htmlmin: {                                     // Task
      dist: {                                      // Target
        options: {                                 // Target options
          removeComments: true,
          collapseWhitespace: true
        },
        files: [{
            expand: true,
            cwd: 'output',
            src: ['**/*.html'],
            dest: 'output'
        }]
      }
    },
    uglify: {
      dist: {
        files: {
          //'output/theme/js/vendor/bootstrap.min.js': ['themes/euler-theme/static/js/vendor/bootstrap.min.js'],
          //'output/theme/js/vendor/jquery.colorbox-min.js': ['themes/euler-theme/static/js/vendor/jquery.colorbox-min.js'],
          //'output/theme/js/vendor/jquery-1.9.1.min.js': ['themes/euler-theme/static/js/vendor/jquery-1.9.1.min.js'],
          'output/theme/js/vendor/modernizr-output.js': ['output/theme/js/vendor/modernizr-output.js'],
          'output/theme/js/jquery.captions.js': ['output/theme/js/jquery.captions.js'],
          'output/theme/js/main.js': ['output/theme/js/main.js']
        }
      }
    }
  });

  // Load the plugins
  grunt.loadNpmTasks('grunt-purifycss');
  grunt.loadNpmTasks('grunt-purgecss');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-modernizr');
  grunt.loadNpmTasks('grunt-contrib-htmlmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s).
  grunt.registerTask('default', ['purgecss:my_target','purifycss','clean:css','clean:js', 'modernizr:dist', 'htmlmin:dist', 'uglify']);

};