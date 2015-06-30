'strict mode';

var mainModule = angular.module('core');

mainModule.run(['customizationService', 'coreFieldService',
  function(customizationService, coreFieldService) {
    var topNavLeft = customizationService.getTopNavElementSet('core_mainTopLeft');

    topNavLeft.addTopNavElement('support',
      function() {
        return {
          title: 'Support',
          type: 'link',
          path: 'https://stage2.advactfdev.com/sf/projects/support'
        }
      }
    );

    topNavLeft.addTopNavElement('metrics',
      function() {
        return {
          title: 'Metrics',
          type: 'link',
          path: 'https://stage2.advactfdev.com/sf/projects/metrics'
        }
      }
    );

    topNavLeft.reorderTopNavElements(function() {
      return ['projects', 'admin', 'myWorkspace', 'support', 'metrics', 'moreLinks', 'history'];
    });

  }
]);
