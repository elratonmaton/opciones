import logging
import os
import uuid

from PIL import Image
from django.core.management import BaseCommand
from django.db.transaction import atomic
from django.utils.text import slugify

from company.models import Slider, Company
from opciones.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with atomic():
            try:
                mode = 0o777
                os.mkdir('{}/company'.format(os.path.join(BASE_DIR, 'media')), mode)
                os.mkdir('{}/company/logos'.format(os.path.join(BASE_DIR, 'media')), mode)
                os.mkdir('{}/company/blocks'.format(os.path.join(BASE_DIR, 'media')), mode)
                os.mkdir('{}/company/sliders'.format(os.path.join(BASE_DIR, 'media')), mode)

                company1: Company = Company()
                company1.name = 'Opciones'
                company1.slug = slugify(company1.name)
                company1.heading = 'Ingeniería y Tecnología Ambiental'
                company1.home_link_more = 'Conoce más'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'opcion_logo.png')
                image = Image.open(image_file)
                new_name = 'company/logos/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.home_logo = new_name

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_1.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.image_block_1 = new_name
                company1.description_title = 'Opciones Ingeniería y Tecnología Ambiental es una empresa peruana, ubicada en la ciudad de Arequipa.'
                company1.description = 'Somos especialistas en mantenimiento de áreas verdes, sistemas de riego tecnificado, habilitaciones urbanas, fumigación, venta de plantas, paisajismo y diseño de áreas verdes a todo nivel.'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_2.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.image_block_2 = new_name
                company1.description_block_2 = 'Nos encontramos en una etapa de desarrollo de tecnologías eficientes con características de auto-sostenibilidad energética y telecontrol de largo alcance, con el fin de anticiparse a los cambios del entorno y poder proporcionar soluciones integrales bajo estándares de calidad y seguridad en el trabajo.'

                company1.title_block_3 = 'Proyectos de innovación tecnologíca'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_3.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.image_block_3 = new_name

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_3_bg.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.background_block_3 = new_name

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_3_logo.png')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company1.logo_company_block_3 = new_name
                company1.description_title_block_3 = 'Es un prototipo desarrollado y ejecutado por Opciones Ingenierí a y Tecnología Ambiental, proyecto de innovación tecnológica – sostenible, que nace del análisis realizado durante el mantenimiento de áreas verdes en diferentes zonas y dimensiones, en la región Arequipa.'
                company1.description_block_3 = 'El objetivo de este robot es ofrecer diagnóstico, y automatización durante el mantenimiento de áreas verdes.\n\nGracias al cofinanciamiento de Innóvate Perú, desarrollamos este prototipo con éxito, en este momento estamos añadiendo mejoras luego de las pruebas realizadas en diferentes terrenos.'

                company1.company_web_page_link = '#'
                company1.company_web_page_name = 'ENTRA A NUESTRA PÁGINA'
                company1.save()

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'slider_company_1.jpg')
                image = Image.open(image_file)
                new_name = 'company/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'Desarrollamos tecnologías'
                slider.subtitle = 'para soluciones eficaces'
                slider.image = new_name
                slider.company = company1
                slider.save()

                #company2
                company2: Company = Company()
                company2.name = 'Paredes'
                company2.slug = slugify(company2.name)
                company2.heading = 'constructora e inmobiliaria'
                company2.home_link_more = 'Conoce más'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_2_logo.png')
                image = Image.open(image_file)
                new_name = 'company/logos/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.home_logo = new_name

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_2_block_2.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.image_block_1 = new_name
                company2.description_title = 'Haremos realidad tus sueños. Nos encargaremos de diseñar, construir y comercializar proyectos residenciales y comerciales, con estándares internacionales de calidad y diseños arquitectónicos modernos y seguros.'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_1_block_2.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.image_block_2 = new_name
                company2.description_title_block_2 = 'Somos Constructores y vendedores directos, la mejor opción para comprar de manera segura.'
                company2.description_block_2 = 'Garantizamos la ejecución de cada proyecto pues dirigimos, supervisamos y planificamos cada etapa de la construcción de acuerdo a todos los estándares exigidos.'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'house.png')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.icon_1_block_4 = new_name
                company2.title_1_block_4 = 'Construcción de calidad'
                company2.description_1_block_4 = 'Nuestro esfuerzo se enfoca en ofrecer construcciones seguras.'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'house_2.png')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.icon_2_block_4 = new_name
                company2.title_2_block_4 = 'Garantía de cumplimiento'
                company2.description_2_block_4 = 'Nuestras entregas estarán regidas por cronogramas muy detallados tanto en áreas técnicas, financieras y legales, lo que permite que se cumpla con el tiempo estimado de entrega de los proyectos.'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'building.png')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company2.icon_3_block_4 = new_name
                company2.title_3_block_4 = 'Inmmuebles listos para vivir'
                company2.description_3_block_4 = 'Nuestras construcciones trae conceptos innovadores, modernos y funcionales, deacuerdo a tus necesidades. '

                company2.company_web_page_link = '#'
                company2.company_web_page_name = 'ENTRA A NUESTRA PÁGINA'
                company2.save()

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_2_slider.jpg')
                image = Image.open(image_file)
                new_name = 'company/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'Construimos con responsabilidad'
                slider.subtitle = 'tu hogar para siempre'
                slider.image = new_name
                slider.company = company2
                slider.save()

                #company3
                company3: Company = Company()
                company3.name = 'El Jardín de Nelly'
                company3.slug = slugify(company3.name)
                company3.heading = 'vivero tiabaya'
                company3.home_link_more = 'Conoce más'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_3_logo.png')
                image = Image.open(image_file)
                new_name = 'company/logos/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company3.home_logo = new_name

                company3.block_1_video = '-5u5RIgDvLc'
                company3.description_title = 'Inspirado en nuestra madre Nelly, que hasta el día de hoy va a la chacra, dedica su tiempo a la naturaleza y todo lo que ella le provee. Gracias a ella, nosotros y nuestros hijos, amamos las plantas; por ello compartimos esta pasión con todas las personas que nos visitan.'

                company3.middle_message = 'En el Jardín de Nelly nos especializamos en la <b>producción, aclimatación y venta de plantas ornamentales.</b>'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_3_block_2.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company3.image_block_2 = new_name
                company3.description_title_block_2 = 'Tenemos una gran variedad de flores, plantas, arbustos, abonos orgánicos, semillas, frutales y macetas con la misma calidad y garantía que hace 10 años.'
                company3.description_block_2 = 'Somos asesores en el diseño de jardines, áreas verdes, cascadas, caídas de agua, piletas, cataratas, riego tecnificado  y por aspersión a mediana y gran escala.'

                company3.company_web_page_link = '#'
                company3.company_web_page_name = 'ENTRA A NUESTRA PÁGINA'
                company3.save()

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_3_slider.jpg')
                image = Image.open(image_file)
                new_name = 'company/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'DONDE RESPIRAS OTRO AIRE'
                slider.subtitle = 'QUE TE ALEGRA LA VIDA'
                slider.image = new_name
                slider.company = company3
                slider.save()


                # company4
                company4: Company = Company()
                company4.name = 'Labora'
                company4.slug = slugify(company4.name)
                company4.heading = 'intermediación laboral'
                company4.home_link_more = 'Conoce más'

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_4_logo.png')
                image = Image.open(image_file)
                new_name = 'company/logos/{}.png'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company4.home_logo = new_name

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_4_block_1.jpg')
                image = Image.open(image_file)
                new_name = 'company/blocks/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                company4.image_block_1 = new_name
                company4.description_title = 'Gestionamos el talento humano, ofreciendo soluciones modernas a través de servicios de procesos de intermediación laboral, búsqueda y selección de personal, y administración de planillas.'
                company4.save()

                image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'company_4_slider.jpg')
                image = Image.open(image_file)
                new_name = 'company/sliders/{}.jpg'.format(uuid.uuid4())
                new_url = '{}/{}'.format(os.path.join(BASE_DIR, 'media'), new_name)
                image.save(new_url)
                slider: Slider = Slider()
                slider.title = 'Gestionamos'
                slider.subtitle = 'el talento humano'
                slider.image = new_name
                slider.company = company4
                slider.save()

                self.stdout.write(self.style.SUCCESS('success'))
            except Exception as e:
                logger.error(e)
                self.stdout.write(self.style.ERROR(e))
