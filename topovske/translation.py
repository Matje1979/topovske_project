from modeltranslation.translator import register, TranslationOptions, translator

from topovske.models import Project, Index, Camp, Archive, Victim, Location


class IndexTranslationOptions(TranslationOptions):
    fields = ('title', 'lead', 'text', 'image_text')


translator.register(Index, IndexTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(Project, ProjectTranslationOptions)


class CampTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(Camp, CampTranslationOptions)


class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title', 'source', 'category',)


translator.register(Archive, ArchiveTranslationOptions)


class VictimTranslationOptions(TranslationOptions):
    fields = ('nationality',)


translator.register(Victim, VictimTranslationOptions)


class LocationTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Location, LocationTranslationOptions)

