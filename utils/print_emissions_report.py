import logging

logger = logging.getLogger(__name__)


def print_emissions_report(emissions_data):
    logger.info(f"\n")
    logger.info(f"### Emission Report for Each Step ###")
    for key, emission in emissions_data.items():
        logger.info(f'Step: {key} - Duration(sec): {emission.duration} - '
                    f'Energy(KWh): {emission.emissions} - Emission CO2(Kg): {emission.energy_consumed}')

    logger.info(f"\n")
    logger.info(f"### Emission Report ###")
    duration_total = emissions_data["data_preprocessing"].duration + emissions_data["training"].duration + \
                     emissions_data["validation"].duration + emissions_data["prediction"].duration
    energy_total = emissions_data["data_preprocessing"].energy_consumed + emissions_data["training"].energy_consumed + \
                   emissions_data["validation"].energy_consumed + emissions_data["prediction"].energy_consumed
    emission_co2_total = emissions_data["data_preprocessing"].emissions + emissions_data["training"].emissions + \
                         emissions_data["validation"].emissions + emissions_data["prediction"].emissions
    logger.info(f'Duration(sec): {duration_total} - '
                f'Energy(KWh): {energy_total} - '
                f'Emission CO2(Kg): {emission_co2_total}')
