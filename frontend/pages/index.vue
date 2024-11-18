<template lang="pug">
v-container.px-0.py-0(fluid)
  v-card(flat tile height="100vh")
    v-card-title.primary.white--text.justify-center Tumor diagnosis
    v-card-text
      v-form(ref="form")
        v-row.justify-center(dense)
          v-col.primary--text.mt-4(cols="12") Diagnóstico de tumores
          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.radiusMean" label="Radius Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.textureMean" label="Texture Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.perimeterMean" label="Perimeter Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.areaMean" label="Area Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.smoothnessMean" label="Smoothness Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.compactnessMean" label="Compactness Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavityMean" label="Concavity Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavePointsMean" label="Concave Points Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.symmetryMean" label="Symmetry Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="5")
            v-text-field(v-model="form.fractalDimensionMean" label="Fractal Dimension Mean"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="3")
            v-text-field(v-model="form.radiusSe" label="Radius Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.textureSe" label="Texture Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.perimeterSe" label="Perimeter Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.areaSe" label="Area Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.smoothnessSe" label="Smoothness Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.compactnessSe" label="Compactness Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavitySe" label="Concavity Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavePointsSe" label="Concave Points Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.symmetrySe" label="Symmetry Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.fractalDimensionSe" label="Fractal Dimension Se"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.radiusWorst" label="Radius Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.textureWorst" label="Texture Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.perimeterWorst" label="Perimeter Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.areaWorst" label="Area Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.smoothnessWorst" label="Smoothness Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.compactnessWorst" label="Compactness Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavityWorst" label="Concavity Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.concavePointsWorst" label="Concave Points Worst"
            hide-details filled depressed)

          v-col(cols="12" md="2" sm="4")
            v-text-field(v-model="form.symmetryWorst" label="Symmetry Worst"
            hide-details filled depressed)

          v-col(cols="12" md="3" sm="5")
            v-text-field(v-model="form.fractalDimensionWorst" label="Fractal Dimension Worst"
            hide-details filled depressed)

    v-card-actions.justify-center.py-5
      v-btn(outlined color="primary" @click="cleanValues()") Limpiar valores
      v-btn(color="info" @click="testDialog=true") Valores de prueba
      v-btn(color="primary" @click="getPrediction()") Predecir

  //- Diálogo para mostrar los resultados de la predicción
  v-dialog(v-model="resultsDialog" max-width="500")
    v-card.pb-3
      v-card-title.white--text(:class="prediction === 1 ? 'primary' : 'info'")
        | Resultados de predicción
        v-spacer
        v-btn(color="white" icon @click="resultsDialog=false")
          v-icon mdi-close

      v-card-text.pt-4
        p.mb-0
          | De acuerdo con nuestra IA, para los datos proporcionados es muy
          | probable que se trate de un tumor
          span.font-weight-bold {{ prediction === 1 ? ' BENIGNO.' : ' MALIGNO.' }}

        p.mb-0.pt-2
          | Resultado de predicción: {{' '}}
          span.font-weight-bold {{ prediction  }}.

        p.mb-0.pt-2
          | Recordar igualmente que el paciente debe ser evaluado por un
          | especialista con el fin de corrobar la información.

      v-card-actions
        v-spacer
        v-btn(@click="resultsDialog=false") Cerrar

  //- Diálogo para seleccionar el tipo de tumor que con el que se desea probar la app
  v-dialog(v-model="testDialog" max-width="500")
    v-card.pb-4
      v-card-title.primary.white--text Establecer valores de prueba
        v-spacer
        v-btn(icon color="white" @click="testDialog=false")
          v-icon mdi-close
      v-card-text.pt-4
        | Seleccione para qué tipo de tumor desea generar los valores de prueba
        | para visualizar cómo responde el aplicativo:

      v-card-actions
        v-spacer
        v-btn(@click="testDialog=false") Cancelar
        v-btn(color="primary" @click="setBenignValues()") Benigno
        v-btn(color="info" @click="setMalignantValues()") Maligno

  //- Overlay para pantalla de carga de la respuesta del backend
  v-overlay(v-model="overlay")
    v-card.primary.px-12.py-3
      v-card-text.text-center
        v-progress-circular.mb-8(indeterminate color="white" size="48")
        p.mb-0.text-subtitle-1 Un momento mientras la IA calcula la predicción
      v-card-actions.justify-center
        v-btn(outlined color="white" @click="overlay=false") Cancelar predicción

  .text-caption.text-center.pt-4
    | Desarrollado por Juan Diego Cobo Cabal y Brayan Alexander Muñoz
    | para el curso de Aprendizaje Automático dictado por Francisco Mercado
    | de la Universidad Autónoma de Occidente.

  .text-caption.text-center.pb-4
    | &copy; 2024. All rights reserved.
</template>

<script>
export default {
  name: 'IndexPage',
  data: () => {
    return {
      prediction: null,
      resultsDialog: true,
      testDialog: false,
      overlay: false,
      form: {
        radiusMean: '13.54',
        textureMean: '14.36',
        perimeterMean: '87.46',
        areaMean: '566.3',
        smoothnessMean: '0.09779',
        compactnessMean: '0.08129',
        concavityMean: '0.06664',
        concavePointsMean: '0.04781',
        symmetryMean: '0.1885',
        fractalDimensionMean: '0.05766',
        radiusSe: '0.2699',
        textureSe: '0.7886',
        perimeterSe: '2.058',
        areaSe: '23.56',
        smoothnessSe: '0.008462',
        compactnessSe: '0.0146',
        concavitySe: '0.02387',
        concavePointsSe: '0.01315',
        symmetrySe: '0.0198',
        fractalDimensionSe: '0.0023',
        radiusWorst: '15.11',
        textureWorst: '19.26',
        perimeterWorst: '99.7',
        areaWorst: '711.2',
        smoothnessWorst: '0.144',
        compactnessWorst: '0.1773',
        concavityWorst: '0.239',
        concavePointsWorst: '0.1288',
        symmetryWorst: '0.2977',
        fractalDimensionWorst: '0.07259'
      }
    }
  },
  methods: {
    async getPrediction () {
      try {
        this.overlay = true
        this.prediction = (await this.$axios.$post('/api/', this.form)).prediction
        this.overlay = false
        this.resultsDialog = true
      } catch (err) {
        // eslint-disable-next-line no-console
        console.log(err)
      }
    },
    cleanValues () {
      this.$refs.form.reset()
      this.$refs.form.resetValidation()
    },
    setBenignValues () {
      this.form = {
        radiusMean: '13.54',
        textureMean: '14.36',
        perimeterMean: '87.46',
        areaMean: '566.3',
        smoothnessMean: '0.09779',
        compactnessMean: '0.08129',
        concavityMean: '0.06664',
        concavePointsMean: '0.04781',
        symmetryMean: '0.1885',
        fractalDimensionMean: '0.05766',
        radiusSe: '0.2699',
        textureSe: '0.7886',
        perimeterSe: '2.058',
        areaSe: '23.56',
        smoothnessSe: '0.008462',
        compactnessSe: '0.0146',
        concavitySe: '0.02387',
        concavePointsSe: '0.01315',
        symmetrySe: '0.0198',
        fractalDimensionSe: '0.0023',
        radiusWorst: '15.11',
        textureWorst: '19.26',
        perimeterWorst: '99.7',
        areaWorst: '711.2',
        smoothnessWorst: '0.144',
        compactnessWorst: '0.1773',
        concavityWorst: '0.239',
        concavePointsWorst: '0.1288',
        symmetryWorst: '0.2977',
        fractalDimensionWorst: '0.07259'
      }
      this.testDialog = false
    },
    setMalignantValues () {
      this.form = {
        radiusMean: '17.99',
        textureMean: '10.38',
        perimeterMean: '122.8',
        areaMean: '1001',
        smoothnessMean: '0.1184',
        compactnessMean: '0.2776',
        concavityMean: '0.3001',
        concavePointsMean: '0.1471',
        symmetryMean: '0.2419',
        fractalDimensionMean: '0.07871',
        radiusSe: '1.095',
        textureSe: '0.9053',
        perimeterSe: '8.589',
        areaSe: '153.4',
        smoothnessSe: '0.006399',
        compactnessSe: '0.04904',
        concavitySe: '0.05373',
        concavePointsSe: '0.01587',
        symmetrySe: '0.03003',
        fractalDimensionSe: '0.006193',
        radiusWorst: '25.38',
        textureWorst: '17.33',
        perimeterWorst: '184.6',
        areaWorst: '2019',
        smoothnessWorst: '0.1622',
        compactnessWorst: '0.6656',
        concavityWorst: '0.7119',
        concavePointsWorst: '0.2654',
        symmetryWorst: '0.4601',
        fractalDimensionWorst: '0.1189'
      }
      this.testDialog = false
    }
  }
}
</script>
