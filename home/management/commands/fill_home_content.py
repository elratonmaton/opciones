import logging
import os
import uuid

from PIL import Image
from django.core.management import BaseCommand
from django.db.models import Q
from django.db.transaction import atomic

from home.models import Slider, AboutUs, Mision, Vision, SocialResponsability
from opciones.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with atomic():
            try:
                mode = 0o777
                os.mkdir('{}/home'.format(os.path.join(BASE_DIR, 'media')), mode)
                os.mkdir('{}/home/sliders'.format(os.path.join(BASE_DIR, 'media')), mode)
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'home_banner-80.jpg')
                image = Image.open(image_file)
                new_name = 'home/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'Creando opciones'
                slider.subtitle = 'para un futuro innovador'
                slider.image = new_name
                slider.save()

                new_name = 'home/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'Creando opciones'
                slider.subtitle = 'para un futuro innovador'
                slider.image = new_name
                slider.save()

                about_us: AboutUs = AboutUs()
                about_us.title = 'NOSOTROS'
                about_us.subtitle = '¿Quienes somos?'
                about_us.description = 'Somos una empresa arequipeña con más de 15 años en el mercado ofreciendo innovación de tecnología aplicada en cada una de nuestras empresas que opera en todo el Perú.'
                about_us.description2 = 'Adaptamos nuestro servicio rápidamente a las necesidades y requerimientos del mercado, y esto nos ha permitido producir y dar una mayor variedad de soluciones a la medida de nuestros clientes.'
                about_us.save()

                os.mkdir('{}/home/mission'.format(os.path.join(BASE_DIR, 'media')))
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mision_image.jpg')
                image = Image.open(image_file)
                new_name = 'home/mission/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                mission: Mision = Mision()
                mission.image = new_name
                mission.description = 'Ofrecemos soluciones integrales a través de servicios diferenciados y de calidad.'
                mission.description2 = 'Desarrollamos nuevas tecnologías y capacitamos permanentemente a nuestro personal para ser la primera opción del mercado y de nuestros propios clientes.'
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'signature.png')
                image = Image.open(image_file)
                new_name = 'home/mission/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                mission.signature = new_name
                mission.save()

                os.mkdir('{}/home/vision'.format(os.path.join(BASE_DIR, 'media')))
                vision: Vision = Vision()
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vision_image.jpg')
                image = Image.open(image_file)
                new_name = 'home/vision/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                vision.image = new_name
                vision.description = 'Nos anticipamos y adaptamos a los cambios que demande el entorno. Por eso nuestros clientes confían en nosotros.'
                vision.description2 = 'Aseguramos la mejora continua en nuestros procesos con miras a la sostenibilidad, automatización tecnológica y especialización. Garantizamos la calidad no solo de nuestro trabajo sino de cada material y proveedor elegido para ofrecer lo mejor y de esta manera posicionarnos sólidamente a nivel nacional.'
                vision.save()

                os.mkdir('{}/home/social'.format(os.path.join(BASE_DIR, 'media')))
                social: SocialResponsability = SocialResponsability()
                social.title = 'Responsabilidad social'
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'social_1.jpg')
                image = Image.open(image_file)
                new_name = 'home/social/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                social.block_1_image = new_name
                social.block_1_description_title = 'La pandemia hizo que nos esforcemos más, por nuestros clientes y para poner el hombro apoyando a otras personas, sin dejar a los nuestros por supuesto. Por ello Iniciamos el proyecto: Opciones Delivery.'
                social.block_1_description = 'Parte de nuestras oficinas se convirtieron  en almacén. Muchos centros y empresas de abasto mayorista se convirtieron en algunos de nuestros principales proveedores.'
                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'social_2.jpg')
                image = Image.open(image_file)
                new_name = 'home/social/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                social.block_2_image = new_name
                social.block_2_description_title = 'Dimos apoyo a productores locales, agricultores de nuestro distrito comprándoles sus productos y distribuyéndolas a diversas instituciones como: albergues de niños y ancianos, entre otros.'
                social.save()

                self.stdout.write(self.style.SUCCESS('success'))
            except Exception as e:
                logger.error(e)
                self.stdout.write(self.style.ERROR(e))
