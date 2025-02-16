from site_setup.models import SiteSetup 

def context_processor_example(request):
  return {
    'example': 'context_processor_example'
  }

def site_setup(request):

  setup = SiteSetup.objects.filter().first

  return {
    'site_setup': setup,
  }