import os
import nltk
import json
import gensim


def getSentences(directory):
		data = []
		ll = ""
		print("hello")
		for subdir, dirs, files in os.walk(self.filename):
			for fil in files:
				print(os.path.join(subdir,fil))
				f = open(os.path.join(subdir,fil),'r')
				for line in f:
					data = json.loads(line)
					print(data)
					ll = ll + [i for i in unicode(data, 'utf-8').lower().split()]
			
			print (ll)
		yield ll


#get = getSentences("extracted")
#get.next()

import json
import os
import re
import sys
from os import walk
import multiprocessing
from gensim.models import word2vec

#generates list of list of words.
def json_readr(path):
    neg_titles=["Dance", "History_of_dance", "List_of_dance_style_categories", "List_of_national_dances", "List_of_ethnic,_regional,_and_folk_dances_by_origin", "List_of_dance_occupations","Choreography","Outline_of_dance","Dance_move","Dance_technology","List_of_dance_companies","List_of_dancers","Group_dance","Dance_and_health","Dancing_mania"
               ,"Modern_dance","Dance_education","Dance_in_mythology_and_religion","Dance_therapy","Dance_music", "First-person_shooter", "Category:First-person_shooters", "Doom_(1993_video_game)", "Counter-Strike_(video_game)", "Wolfenstein_3D", "Call_of_Duty", "Quake_(video_game)", "Battlefield_(video_game_series)", "First-person_shooter_engine", "Multiplayer_video_game", "Action_game", "Shooter_game", "Esports", "Arrow_keys#WASD_keys", "Computer_mouse", "Computer_keyboard", "Reticle", "Level_(video_gaming)", "Weapon", "Hitscan",
"ADHD_rating_scale","Abnormal_psychology","Abreaction","Accelerated_experiential_dynamic_psychotherapy","Acceptance_and_commitment_therapy","Acute_stress_disorder","Acute_stress_reaction","Addiction_psychiatry","Adjustment_disorder","Adventure_therapy","Agoraphobia","Aichmophobia","Alcohol_abuse","Alcohol_dependence","Alcohol_withdrawal","Alcoholic_hallucinosis","Alcoholism","Alzheimer%27s_disease",
"Amafufunyana","American_Academy_of_Child_and_Adolescent_Psychiatry","American_Board_of_Psychiatry_and_Neurology","American_Neuropsychiatric_Association","American_Psychiatric_Association","Amnesia","Amphetamine_dependence","Analytical_psychology","Angelman_syndrome","Animal-assisted_therapy",
"Anorexia_nervosa","Anorgasmia","Anosognosia","Antenatal_depression","Anterograde_amnesia","Anti-psychiatry","Anti-social_behaviour",
"Antisocial_personality_disorder","Anxiety_disorder","Anxiolytic","Applied_behavior_analysis","Applied_psychology","Art_therapy","Asperger_syndrome","Atelophobia","Athens_insomnia_scale","Attachment-based_psychotherapy","Attachment-based_therapy_(children)",
"Attachment_therapy","Attack_therapy","Attention_deficit_disorder","Attention_deficit_hyperactivity_disorder","Atypical_depression","Autism","Autism_spectrum","Autogenic_training","Autophagia","Aversion_therapy","Avoidant/restrictive_food_intake_disorder","Avoidant_personality_disorder","Barbiturate_dependence","Basic_science_(psychology)",
"Behavior_modification","Behavioral_activation","Behavioral_addiction","Behavioral_medicine","Behavioral_neuroscience","Behaviour_therapy","Behavioural_genetics","Benzodiazepine_dependence","Benzodiazepine_misuse","Benzodiazepine_withdrawal","Bibliomania","Bibliotherapy","Binge_eating_disorder","Bioenergetic_analysis","Biofeedback","Biological_psychiatry","Bipolar_II_disorder","Bipolar_I_disorder","Bipolar_disorder","Body_dysmorphic_disorder","Body_integrity_dysphoria","Body_psychotherapy","Borderline_intellectual_functioning","Borderline_personality_disorder","Brief_psychotherapy","Brief_psychotic_disorder","Brief_reactive_psychosis","Bulimia_nervosa","Caffeine-induced_anxiety_disorder","Caffeine-induced_sleep_disorder",
"Cambridge_Somerville_Youth_Study","Campaign_Against_Psychiatric_Abuse","Cannabis_dependence","Catatonia","Cerebral_palsy","Chess_therapy","Child_and_adolescent_psychiatry","Child_psychotherapy","Childhood_disintegrative_disorder","Chinese_Society_of_Psychiatry","Circadian_rhythm_sleep_disorder","Classical_Adlerian_psychotherapy","Claustrophobia","Clinical_Depression","Clinical_formulation","Clinical_neuroscience","Clinical_psychology","Closed-head_injury","Clouding_of_consciousness","Cluttering","Co-counselling","Cocaine_dependence","Cocaine_intoxication","Cognitive_analytic_therapy","Cognitive_behavior_therapy","Cognitive_disorder","Cognitive_neuropsychiatry","Cognitive_psychology","Cognitive_therapy","Cognitivism_(psychology)","Coherence_therapy","Collaborative_therapy","Communication_disorder","Community_psychology","Comparative_psychology","Compassion_focused_therapy","Compulsive_behavior","Concentrative_movement_therapy","Concussion","Conduct_disorder","Consumer_behaviour","Contemplative_psychotherapy","Contextual_therapy","Conversational_model","Conversion_disorder","Conversion_therapy","Cotard_delusion","Counseling","Counseling_psychology","Creutzfeldt%E2%80%93Jakob_disease","Critical_psychology","Cross-cultural_psychiatry","Cross-cultural_psychology","Cultural_psychology","Cyclothymia","Da_Costa%27s_syndrome","Dance_movement_therapy","Dance_therapy",
"Daseinsanalysis","Delayed_ejaculation","Delirium","Delirium_tremens","Delusional_disorder","Delusional_parasitosis","Dementia","Dementia_with_Lewy_bodies","Democratic_Psychiatry","Dependent_personality_disorder","Depersonalization_disorder","Depression_(mood)","Depressive_personality_disorder","Depth_psychology","Derealization","Dermatillomania","Dermatophagia","Descriptive_psychiatry","Desynchronosis","Developmental_Needs_Meeting_Strategy","Developmental_coordination_disorder","Developmental_disability","Developmental_disorder","Developmental_psychology","Developmental_regression","Diagnosis_of_schizophrenia","Diagnostic_and_Statistical_Manual_of_Mental_Disorders","Diagnostic_overshadowing","Dialectical_behavior_therapy","Differential_psychology","Diogenes_Syndrome","Disinhibited_attachment_disorder","Disinhibited_social_engagement_disorder","Disorganized_schizophrenia","Dispareunia","Disruptive_Behavior_Disorders_Rating_Scale","Disruptive_mood_dysregulation_disorder","Dissociative_disorder","Dissociative_identity_disorder","Drama_therapy","Dreamwork","Drug_overdose","Drug_withdrawal","Dual-role_transvestism","Dyadic_developmental_psychotherapy","Dyscalculia","Dyslexia","Dysthymia","Eating_disorder_not_otherwise_specified","Eating_disorders","Eating_disorders_and_development","Eating_mucus","Eclectic_psychotherapy","Ecological_counseling","Educational_psychology","Effects_of_genocide_on_youth","Ego-dystonic_sexual_orientation","Emergency_psychiatry",
"Emotional_Freedom_Techniques","Emotional_and_behavioral_disorders","Emotionally_focused_therapy","Encopresis","Endogenous_depression","Enemy_complex","Enuresis","Environmental_psychology","Epilepsy","Epworth_Sleepiness_Scale","Erectile_dysfunction","Erotomania","European_Psychiatric_Association","Evolutionary_psychology","Excoriation_disorder","Exhibitionism","Existential_therapy","Experimental_psychology","Exposure_and_response_prevention","Expressive_therapies","Eye_movement_desensitization_and_reprocessing","Factitious_disorder","Factitious_disorder_imposed_on_another","Factitious_disorder_imposed_on_self","Family_Constellations","Family_therapy","Female_sexual_arousal_disorder","Feminist_therapy","Focusing_(psychotherapy)","Folie_%C3%A0_deux","Forensic_psychiatry","Forensic_psychology","Fregoli_delusion","Frontal_Assessment_Battery","Frontotemporal_dementia","Fugue_state","Functional_analytic_psychotherapy","Future-oriented_therapy","Gaming_disorder","Ganser_syndrome",
"Gender_dysphoria","General_adaptation_syndrome","Generalized_anxiety_disorder","Gerda_Boyesen","Geriatric_psychiatry","Gestalt_theoretical_psychotherapy","Gestalt_therapy","Global_Initiative_on_Psychiatry","Globus_pharyngis","Grandiose_delusions","Grief","Grief_counseling","Group_analysis","Group_psychotherapy","Guided_imagery","HIV-associated_neurocognitive_disorder","Hakomi","Hallucinogen","Hallucinogen_persisting_perception_disorder","Health_psychology","High-functioning_autism","History_of_psychology","Histrionic_personality_disorder","Holotropic_Breathwork","Hong_Kong_College_of_Psychiatrists","Human_Givens","Human_factors_and_ergonomics","Humanistic_psychology","Huntington%27s_disease","Hypercalculia","Hyperkinetic_disorder",
"Hyperreligiosity","Hypersexuality","Hypersomnia","Hypnotherapy","Hypnotic","Hypoactive_sexual_desire_disorder","Hypochondriasis","Hypokalemic_sensory_overstimulation","Hypomania","Hypomanic_episode","Hysteria","ICD-10_Chapter_V:_Mental_and_behavioural_disorders","Identity_disorder","Idiopathic_hypersomnia","Imaging_genetics","Immuno-psychiatry","Impulse_control_disorder","Independent_Psychiatric_Association_of_Russia","Indian_Psychiatric_Society","Industrial_and_organizational_psychology","Ingestive_behaviors","Inner_Relationship_Focusing","Insomnia","Integral_psychotherapy","Integrative_body_psychotherapy","Integrative_milieu_model","Integrative_psychotherapy","Intellectual_disability","Intensive_short-term_dynamic_psychotherapy","Intermittent_explosive_disorder","Internal_Family_Systems_Model","Internet_phobia","Interpersonal_psychoanalysis","Interpersonal_psychotherapy","Journal_therapy","Kleptomania","Korsakoff%27s_syndrome","Labeling_theory","Lacunar_amnesia","Late_talker",
"Legal_psychology","Liaison_psychiatry","Logic-based_therapy","Logotherapy","Major_depressive_disorder","Major_depressive_episode","Male_erectile_disorder","Malingering","Mania","Manic_episode","Mass_psychogenic_illness","Mathematical_psychology","Mathematics_disorder","Medical_psychology","Melancholia","Melancholic_depression","Mental_disorder","Mental_health","Mental_health_professional","Mentalization-based_treatment","Metacognitive_therapy","Method_of_levels","Mild_cognitive_impairment","Military_acute_concussion_evaluation","Military_psychiatry","Military_psychology","Mindfulness-based_cognitive_therapy",
"Mindfulness-based_stress_reduction","Minor_depressive_disorder","Misophonia","Mixed_episode","Mode_deactivation_therapy","Mood_disorder","Morita_therapy","Motivational_interviewing","Motor_planning","Multimodal_therapy","Multisystemic_therapy","Multitheoretical_psychotherapy","Munchausen%27s_syndrome","Music_psychology","Music_therapy","Nail_biting","Narcissistic_personality_disorder","Narcolepsy","Narrative_therapy","National_Institute_of_Mental_Health","Neurasthenia","Neurocysticercosis","Neurodevelopmental_disorder","Neuroimaging","Neurological_disorder","Neurophysiology","Neuropsychiatry","Neuropsychology","Nicotine_withdrawal","Night_eating_syndrome","Night_terror","Nightmare","Nightmare_disorder","Nonverbal_learning_disorder","Nonviolent_Communication","Nosophobia","Nouthetic_counseling","Nude_psychotherapy","Object_relations_theory","Obsessive%E2%80%93compulsive_disorder","Obsessive%E2%80%93compulsive_personality_disorder","Obsessive-compulsive_disorder","Obsessive-compulsive_personality_disorder",
"Occupational_health_psychology","Occupational_therapy_in_the_management_of_seasonal_affective_disorder","Ondine%27s_curse","Oneirophrenia","Onychotillomania","Opioid","Opioid_dependence","Oppositional_defiant_disorder","Organic_mental_disorders","Orthodox_psychotherapy","Orthorexia","Other_specified_feeding_or_eating_disorder","Outline_of_psychology","Outline_of_the_psychiatric_survivors_movement","Pain_disorder","Pain_management","Palliative_medicine","Panic_disorder","Paranoid_personality_disorder","Paraphilia","Parasomnia","Parent%E2%80%93child_interaction_therapy",
"Parent_management_training","Parkinson%27s_Disease","Parkinson%27s_disease","Partialism","Pastoral_counseling","Pathological_gambling","Penetrating_head_injury","Persecutory_delusion","Person-centered_therapy","Personality_disorder",
"Personality_psychology","Pervasive_developmental_disorder","Pervasive_developmental_disorder_not_otherwise_specified","Phencyclidine","Philadelphia_Association","Philosophy_of_psychiatry","Phobia","Phobic_disorder","Phonological_disorder","Physical_abuse","Physical_dependence","Pica_(disorder)","Pick%27s_disease","Play_therapy","Poetry_therapy",
"Political_abuse_of_psychiatry","Political_abuse_of_psychiatry_in_the_Soviet_Union","Political_psychology","Poly_drug_use","Positive_psychology","Positive_psychotherapy","Postpartum_depression","Postpartum_psychosis","Posttraumatic_stress_disorder","Postural_Integration","Pragmatic_language_impairment","Premature_ejaculation","Primal_Integration","Primal_therapy","Primary_age-related_tauopathy","Primary_hypersomnia","Primary_insomnia","Primary_polydipsia","Problem_gambling","Process_oriented_psychology","Process_psychology","Progressive_counting_(PC)","Prolonged_exposure_therapy","Provocative_therapy","Pseudologia_fantastica","Psychedelic_therapy","Psychiatric_diagnosis","Psychiatric_disorders_of_childbirth","Psychiatric_epidemiology","Psychiatric_genetics","Psychiatric_survivors_movement","Psychiatrist","Psychiatry","Psycho-oncology","Psychoanalysis","Psychodrama","Psychodynamic_psychotherapy","Psychogenic_amnesia","Psychogenic_pain","Psychology","Psychology_of_religion","Psychopharmacology","Psychosis","Psychosomatic_medicine","Psychosurgery","Psychosynthesis","Psychotherapy","Psychotic_disorder","Pulsing_(bodywork)","Pyromania","Quantitative_psychology","REM_Sleep_Behavior_Disorder_Screening_Questionnaire","REM_Sleep_Behavior_Disorder_Single-Question_Screen","Rapid_eye_movement_sleep_behavior_disorder","Rational_emotive_behavior_therapy","Rational_living_therapy","Reactive_attachment_disorder","Reality_therapy","Rebirthing-breathwork","Rebound_effect","Recovered-memory_therapy","Recurrent_brief_depression","Reichian_therapy","Relational-cultural_therapy","Relational_disorder",
"Relationship_counseling","Relationship_obsessive%E2%80%93compulsive_disorder","Remote_therapy","Residual_schizophrenia","Restless_legs_syndrome","Retarded_depression","Retrograde_amnesia","Rett_syndrome","Rosenhan_experiment","Royal_Australian_and_New_Zealand_College_of_Psychiatrists","Royal_College_of_Psychiatrists","Rumination_(psychology)","Rumination_syndrome","Sandplay_therapy","Schema_therapy","Schizoaffective_disorder","Schizoid_personality_disorder","Schizophrenia","Schizophreniform_disorder","Schizotypal_personality_disorder","School_psychology","Scopophobia","Seasonal_affective_disorder","Sedative","Selective_mutism","Self-defeating_personality_disorder","Self-enucleation","Self-harm","Sensorimotor_psychotherapy","Separation_anxiety_disorder","Sex_therapy","Sexual_anhedonia","Sexual_dysfunction","Sexual_fetishism","Sexual_identity_therapy","Sexual_masochism_disorder","Sexual_maturation_disorder","Sexual_relationship_disorder","Sexual_sadism_disorder","Shared_psychotic_disorder","Sleep_disorder","Sleep_medicine","Sleep_paralysis","Sleep_sex","Sleep_terror_disorder","Sleepwalking_disorder","Social_anxiety_disorder","Social_phobia","Social_psychology","Social_therapy","Solution_focused_brief_therapy","Somatic_experiencing","Somatic_psychology","Somatic_symptom_disorder","Somatization_disorder","Somatoform_disorder","Specific_phobia","Sport_psychology","Status_dynamic_psychotherapy","Stereotypic_movement_disorder","Stockholm_syndrome","Structural_family_therapy","Stuttering","Subfields_of_psychology","Substance-related_disorder","Supportive_psychotherapy",
"Systematic_desensitization","Systemic_therapy","T-groups","Taiwanese_Society_of_Child_and_Adolescent_Psychiatry","Tardive_dyskinesia","Therapeutic_community","Thought_Field_Therapy","Tic_disorder","Timeline_of_psychology","Tourettes_Syndrome","Traffic_psychology","Transactional_analysis","Transference_focused_psychotherapy","Transient_global_amnesia","Transpersonal_psychology","Transtheoretical_model","Transvestic_disorder","Trichotillomania","Twelve-step_program","Vegetotherapy","Wilderness_therapy",
"Working_Commission_to_Investigate_the_Use_of_Psychiatry_for_Political_Purposes","World_Psychiatric_Association","Writing_therapy","Outline_of_the_psychiatric_survivors_movement"]
    l = []
    for (dirpath, dirnames,filenames) in walk(path):
        for fi in filenames:
            for line in open(os.path.join(dirpath,fi), mode="r",encoding="utf-8"):
                li = []
                a = json.loads(line).get("title")
                if a not in neg_titles:
                    li = []
                    li = json.loads(line).get("text") 
                    z = re.sub(r'[™!®#\'()*+,-./:;<=>?@\&[\]^_`{|}~"’”“′‘\\\\%0123456789£'',\n()]'," ",li)       
                    w = [w.lower() for w in str(z).split()]    
                    l.append(w)              
    yield l 

#train word2vec
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
  
    path = "E:\extracted"    
    model = Word2Vec(json_readr(path), size=400, 
        window=5, min_count=5, workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use (much) less RAM
    model.init_sims(replace=True)
    model.save("novice_word_vec_wiki.model")

# with open('sent_to_train.txt', 'w') as f:
    # for item in lis:
        # f.write("%s\n" % item)
    
